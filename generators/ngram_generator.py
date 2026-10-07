"""
Character N-gram Language Model для генерации ников.

Модель учится P(буква | контекст) на корпусе реальных ников
и генерирует новые через семплинг.
"""

from collections import defaultdict, Counter
import math
import random


class NGramModel:
    """N-gram модель на уровне символов."""

    def __init__(self, order: int = 3, smoothing: float = 0.1):
        """
        Args:
            order: максимальная длина контекста
            smoothing: сглаживание для нулевых вероятностей
        """
        self.order = order
        self.smoothing = smoothing
        self.tables = [defaultdict(Counter) for _ in range(order + 1)]
        self.vocab = Counter()

    def train(self, words: list) -> None:
        """Обучает модель на списке слов."""
        for word in words:
            word = word.lower()
            self.vocab.update(word)
            padded = "^" * self.order + word + "$"
            for i in range(self.order, len(padded)):
                for o in range(1, self.order + 1):
                    ctx = padded[i - o:i]
                    nxt = padded[i]
                    self.tables[o][ctx][nxt] += 1

    def generate(self, temperature: float = 1.0, max_len: int = 12) -> str:
        """Генерирует одно слово."""
        # TODO: реализовать семплинг
        return ""
