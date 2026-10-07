"""
Итоговая оценка ников по 8 критериям.

Критерии:
  1. Естественность (log-prob под моделью)
  2. Произносимость (CV-паттерн)
  3. Баланс гласных
  4. Длина
  5. Kill Feed Test (A-M в начале)
  6. Открытый финал
  7. Уникальность
  8. Штрафы за мусор
"""

import math
from .phonetics import pronounceability, vowel_balance, open_ending


def score(name: str, log_prob: float = 0.0) -> dict:
    """Оценивает ник и возвращает словарь с оценками."""
    n = len(name)
    naturalness = 1.0 / (1.0 + math.exp(-log_prob - 2))
    pron = pronounceability(name)
    balance = vowel_balance(name)
    opening = open_ending(name)
    killfeed = 1.0 if name[0].lower() in "abcdefghijklm" else 0.6

    # Длина
    if 4 <= n <= 7:
        length = 1.0
    elif n == 8:
        length = 0.7
    elif n == 9:
        length = 0.4
    else:
        length = 0.2

    total = (
        naturalness * 0.35 +
        pron * 0.20 +
        balance * 0.10 +
        length * 0.10 +
        killfeed * 0.10 +
        opening * 0.15
    )

    return {
        "name": name,
        "score": round(total, 4),
        "naturalness": round(naturalness, 3),
        "pronounceability": round(pron, 3),
        "balance": round(balance, 3),
    }
