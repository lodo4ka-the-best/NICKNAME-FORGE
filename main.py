"""
Точка входа NICKNAME FORGE.

Использование:
    python main.py --style epic --count 5
    python main.py --style cyber --count 10 --check
    python main.py --style dark --count 5 --check --game dota
"""

import argparse

from core.data_models import Profile
from core.constants import STYLES, PLATFORM_RULES
from interfaces.cli import CLI


def parse_args():
    """Разбирает аргументы командной строки."""
    parser = argparse.ArgumentParser(
        description="NICKNAME FORGE — генератор игровых никнеймов"
    )
    parser.add_argument(
        "--style", default="epic",
        choices=STYLES,
        help="стиль ника",
    )
    parser.add_argument(
        "--count", type=int, default=5,
        help="сколько ников сгенерировать",
    )
    parser.add_argument(
        "--platform", default="default",
        choices=list(PLATFORM_RULES.keys()),
        help="платформа (влияет на правила длины/символов)",
    )
    parser.add_argument(
        "--check", action="store_true",
        help="проверить занятость через DuckDuckGo",
    )
    parser.add_argument(
        "--game", default="esports",
        help="контекст поиска (esports / dota / csgo / valorant / lol)",
    )
    parser.add_argument(
        "--min-len", type=int, default=4,
        help="минимальная длина",
    )
    parser.add_argument(
        "--max-len", type=int, default=12,
        help="максимальная длина",
    )
    parser.add_argument(
        "--threshold", type=float, default=0.60,
        help="порог качества (0-1)",
    )
    parser.add_argument(
        "--seed", type=int, default=42,
        help="сид для воспроизводимости",
    )
    return parser.parse_args()


def main():
    """Главная функция."""
    args = parse_args()

    profile = Profile(
        style=args.style,
        platform=args.platform,
        min_len=args.min_len,
        max_len=args.max_len,
        quality_threshold=args.threshold,
        seed=args.seed,
    )

    # ─── Заголовок ───
    print("=" * 60)
    print("  NICKNAME FORGE")
    print("=" * 60)
    print(f"  Стиль:      {args.style}")
    print(f"  Платформа:  {args.platform}")
    print(f"  Количество: {args.count}")
    print(f"  Проверка:   {'да' if args.check else 'нет'}")
    print("=" * 60)

    # ─── Генерация ───
    cli = CLI(profile)
    results = cli.generate(args.count)

    if not results:
        print("❌ Не удалось сгенерировать ники")
        return

    # ─── Проверка занятости ───
    if args.check:
        print(f"\n🌐 Проверяю через DuckDuckGo ({args.game})...")
        print("   (это займёт ~2 сек на ник)\n")

        from checkers.google_checker import check_google_batch
        names = [r.name for r in results]
        checks = check_google_batch(names, game=args.game, delay=1.5)

        for r, c in zip(results, checks):
            r.is_free = c["is_free"]

    # ─── Вывод ───
    print()
    print("─" * 60)
    print(f"  🎮 {args.style.upper()}")
    print("─" * 60)

    for i, r in enumerate(results, 1):
        bar = "█" * int(r.score * 14)

        # Маркер занятости
        if args.check:
            if r.is_free is True:
                mark = " ✅"
            elif r.is_free is False:
                mark = " ❌"
            else:
                mark = " ❓"
        else:
            mark = ""

        print(f"  {i:>2}. {r.name:<12} {r.score:.3f}{mark}  {bar}")

    # ─── Итог ───
    if args.check:
        free = sum(1 for r in results if r.is_free is True)
        busy = sum(1 for r in results if r.is_free is False)
        unknown = sum(1 for r in results if r.is_free is None)
        print()
        print(f"  Свободно: {free} | Занято: {busy} | Неизвестно: {unknown}")


if __name__ == "__main__":
    main()
