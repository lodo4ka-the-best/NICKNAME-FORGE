"""
Character N-gram Language Model для генерации ников.

Модель учится P(буква | контекст) на корпусе реальных ников
и генерирует новые через семплинг.

Это классический подход из NLP (Jurafsky & Martin, глава 3).
"""

import math
import random
from collections import defaultdict, Counter
from typing import List, Optional


class NGramModel:
    """
    N-gram модель на уровне символов.

    Атрибуты:
        order: максимальная длина контекста (3 = триграммы)
        smoothing: сглаживание для нулевых вероятностей
        tables: таблицы частот для каждого порядка
        vocab: Counter всех букв корпуса
        starts: распределение первых 2 букв
        lengths: распределение длин ников
    """

    def __init__(self, order: int = 3, smoothing: float = 0.1):
        self.order = order
        self.smoothing = smoothing
        self.tables = [defaultdict(Counter) for _ in range(order + 1)]
        self.vocab = Counter()
        self.starts = Counter()
        self.lengths = Counter()
        self.trained = False

    def train(self, words: List[str]) -> None:
        """
        Обучает модель на списке слов.

        Для каждого слова запоминает:
          - контексты всех порядков (1..order)
          - следующую букву после каждого контекста
        """
        for word in words:
            word = word.lower()
            self.vocab.update(word)
            self.lengths[len(word)] += 1

            # padding: ^^^word$
            padded = "^" * self.order + word + "$"

            # Запоминаем начало
            self.starts[padded[self.order:self.order + 2]] += 1

            # Запоминаем контексты
            for i in range(self.order, len(padded)):
                for o in range(1, self.order + 1):
                    ctx = padded[i - o:i]
                    nxt = padded[i]
                    self.tables[o][ctx][nxt] += 1

        self.trained = True

    def _dist(self, order: int, ctx: str) -> dict:
        """P(буква | контекст) для заданного порядка."""
        table = self.tables[order].get(ctx)
        if not table:
            return {}
        total = sum(table.values()) + self.smoothing * len(self.vocab)
        return {
            c: (n + self.smoothing) / total
            for c, n in table.items()
        }

    def _backoff_dist(self, ctx: str) -> dict:
        """
        Backoff: пробуем самый длинный контекст.
        Если для него нет данных — переходим к более короткому.
        """
        for o in range(min(len(ctx), self.order), 0, -1):
            d = self._dist(o, ctx[-o:])
            if d:
                return d

        # Fallback: униграммы
        total = sum(self.vocab.values()) + self.smoothing * len(self.vocab)
        return {
            c: (n + self.smoothing) / total
            for c, n in self.vocab.items()
        }

    def generate(self, temperature: float = 1.0, max_len: int = 12) -> str:
        """
        Генерирует одно слово.

        Args:
            temperature: <1 консервативно, >1 креативно
            max_len: максимальная длина
        """
        if not self.trained:
            return ""

        starts = [s for s in self.starts if s]
        if not starts:
            return ""

        weights = [self.starts[s] for s in starts]
        start = random.choices(starts, weights=weights)[0]

        result = list(start)
        ctx = "^" * self.order + start

        for _ in range(max_len):
            dist = self._backoff_dist(ctx)
            if not dist:
                break

            chars = list(dist.keys())
            probs = [dist[c] for c in chars]

            # Температура
            if temperature != 1.0:
                probs = [p ** (1.0 / temperature) for p in probs]
                total = sum(probs)
                probs = [p / total for p in probs]

            c = random.choices(chars, weights=probs)[0]

            # Конец слова
            if c == "$":
                break

            result.append(c)
            ctx += c

        return "".join(result)

    def log_prob(self, word: str) -> float:
        """
        Логарифм вероятности слова под моделью.
        Используется для оценки "естественности" ника.
        """
        word = word.lower()
        padded = "^" * self.order + word + "$"
        logp = 0.0

        for i in range(self.order, len(padded)):
            dist = self._backoff_dist(padded[:i])
            c = padded[i]
            p = dist.get(c, self.smoothing / (1 + self.smoothing))
            logp += math.log(p)

        return logp / max(len(word), 1)


class NGramGenerator:
    """
    Обёртка над NGramModel — с обучением на корпусе.
    """

    def __init__(self, style: str = "epic", order: int = 3):
        from corpus.nicknames import get_corpus
        self.style = style
        self.model = NGramModel(order=order)
        self.model.train(get_corpus(style))

    def generate_one(self, temperature: float = 0.85,
                     max_len: int = 12) -> str:
        """Генерирует один ник и капитализирует его."""
        raw = self.model.generate(temperature=temperature, max_len=max_len)
        if not raw:
            return ""
        return raw[0].upper() + raw[1:]

    def score_naturalness(self, name: str) -> float:
        """Возвращает естественность ника (0-1)."""
        logp = self.model.log_prob(name)
        return 1.0 / (1.0 + math.exp(-logp - 2))
