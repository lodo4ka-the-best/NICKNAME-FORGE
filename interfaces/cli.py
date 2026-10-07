"""
Интерфейс командной строки.

Собирает все модули вместе: генерация + оценка + проверка.
"""

import random
from typing import List

from core.data_models import Profile, Result
from core.constants import STYLES, PLATFORM_RULES
from core.utils import log
from generators.ngram_generator import NGramGenerator
from scoring.scorer import score
from scoring.platform_rules import is_valid_for
from corpus.nicknames import get_corpus
from corpus.stop_words import is_clean


class CLI:
    """Командный интерфейс."""

    def __init__(self, profile: Profile):
        self.profile = profile
        self.generator = NGramGenerator(style=profile.style)
        self.corpus = get_corpus(profile.style)

        if profile.seed is not None:
            random.seed(profile.seed)

    def _is_valid(self, name: str) -> bool:
        """Полная валидация ника."""
        # Длина
        if not (self.profile.min_len <= len(name) <= self.profile.max_len):
            return False

        # Платформа
        if not is_valid_for(name, self.profile.platform):
            return False

        # Занятые
        if name.lower() in {o.lower() for o in self.profile.occupied}:
            return False

        # Стоп-слова и паттерны
        if not is_clean(name):
            return False

        # Точная копия эталона
        if name.lower() in {c.lower() for c in self.corpus}:
            return False

        # Минимум 3 разные буквы
        if len(set(name.lower())) < 3:
            return False

        return True

    def generate_one(self) -> Result:
        """
        Генерирует один хороший ник.
        Если score < порога — перегенерирует до max_retries.
        """
        best = None

        for _ in range(self.profile.max_retries):
            name = self.generator.generate_one(
                temperature=self.profile.temperature,
                max_len=self.profile.max_len + 2,
            )
            if not name:
                continue

            if not self._is_valid(name):
                continue

            logp = self.generator.model.log_prob(name)
            scored = score(name, log_prob=logp, corpus=self.corpus)

            if best is None or scored["score"] > best.score:
                best = Result(
                    name=name,
                    score=scored["score"],
                    naturalness=scored["naturalness"],
                    pronounceability=scored["pronounceability"],
                    balance=scored["balance"],
                )

            if scored["score"] >= self.profile.quality_threshold:
                return Result(
                    name=name,
                    score=scored["score"],
                    naturalness=scored["naturalness"],
                    pronounceability=scored["pronounceability"],
                    balance=scored["balance"],
                )

        # Не достигли — вернём лучший (если он не мусор)
        if best and best.score >= self.profile.quality_threshold * 0.7:
            return best
        return None

    def generate(self, count: int) -> List[Result]:
        """Генерирует `count` хороших ников."""
        results = []
        used = set()

        for _ in range(count * 10):  # максимум попыток
            if len(results) >= count:
                break
            r = self.generate_one()
            if r is None:
                continue
            if r.name.lower() in used:
                continue
            used.add(r.name.lower())
            results.append(r)

        results.sort(key=lambda r: -r.score)
        return results


def run_cli():
    """Интерактивное меню."""
    print("=" * 60)
    print("  NICKNAME FORGE — CLI")
    print("=" * 60)

    # Стиль
    print(f"\nДоступные стили: {', '.join(STYLES)}")
    style = input("Выбери стиль [epic]: ").strip() or "epic"
    if style not in STYLES:
        log(f"Стиль '{style}' не найден, использую epic", "warn")
        style = "epic"

    # Количество
    count_str = input("Сколько ников? [10]: ").strip() or "10"
    try:
        count = int(count_str)
    except ValueError:
        count = 10

    # Платформа
    platforms = list(PLATFORM_RULES.keys())
    print(f"Доступные платформы: {', '.join(platforms)}")
    platform = input("Платформа [default]: ").strip() or "default"
    if platform not in PLATFORM_RULES:
        log(f"Платформа '{platform}' не найдена, использую default", "warn")
        platform = "default"

    # Профиль
    profile = Profile(
        style=style,
        platform=platform,
        quality_threshold=0.60,
        max_retries=20,
        seed=42,
    )

    # Генерация
    log(f"Генерирую {count} ников в стиле '{style}'...", "info")
    cli = CLI(profile)
    results = cli.generate(count)

    # Вывод
    print()
    print("─" * 60)
    print(f"  🎮 {style.upper()}")
    print("─" * 60)

    if not results:
        log("Не удалось сгенерировать ники. Попробуй снизить порог.", "warn")
        return

    for i, r in enumerate(results, 1):
        bar = "█" * int(r.score * 14)
        print(f"  {i:>2}. {r.name:<12} {r.score:.3f}  "
              f"[естеств:{r.naturalness:.2f} "
              f"произн:{r.pronounceability:.2f}]  {bar}")

    print("\nПроверка занятости:")
    print("  1. Google (универсальная)")
    print("  2. Minecraft")
    print("  3. Roblox")
    print("  4. Не проверять")
    choice = input("Выбор [1]: ").strip() or "1"

    if choice == "1":
        from checkers.ddg_checker import check_google_batch
        checks = check_google_batch([r.name for r in results])
        for r, c in zip(results, checks):
            r.is_free = c["is_free"]
            r.platform = "google"
    elif choice == "2":
        from checkers.universal import check_all
        checks = check_all([r.name for r in results], "minecraft")
        for r, c in zip(results, checks):
            r.is_free = c["is_free"]
            r.platform = "minecraft"


if __name__ == "__main__":
    run_cli()
