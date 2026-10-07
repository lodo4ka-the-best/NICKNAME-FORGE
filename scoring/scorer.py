"""
Итоговая оценка ников по 8 критериям.

Критерии:
  1. Естественность (log-prob под моделью)
  2. Произносимость (CV-паттерн)
  3. Баланс гласных
  4. Длина
  5. Kill Feed Test
  6. Открытый финал
  7. Уникальность относительно корпуса
  8. Штрафы за мусор
"""

import re
from typing import Optional

from .phonetics import (
    pronounceability,
    vowel_balance,
    open_ending,
    kill_feed_bonus,
    length_score,
)

# Веса критериев (сумма = 1.0)
WEIGHTS = {
    "naturalness": 0.30,
    "pronounceability": 0.20,
    "balance": 0.10,
    "length": 0.10,
    "killfeed": 0.10,
    "opening": 0.10,
    "uniqueness": 0.10,
}


def compute_penalty(name: str) -> float:
    """
    Штрафы за мусор. Возвращает множитель от 0.1 до 1.0.
    Чем больше мусора — тем ниже множитель.
    """
    penalty = 1.0
    low = name.lower()

    # 4+ согласных подряд
    if re.search(r"[bcdfghjklmnpqrstvwxz]{4,}", low):
        penalty *= 0.5

    # Мёртвые кластеры в начале
    if re.match(r"^(nm|tn|ps|ks|pf|bv|dv|fv|gv|kv|pv|tv|zv|mn|pn|bn)", low):
        penalty *= 0.6

    # Мало разных букв
    if len(set(low)) < 4:
        penalty *= 0.7

    # Много цифр
    digits = sum(c.isdigit() for c in name)
    if digits > 2:
        penalty *= 0.4
    elif digits == 2:
        penalty *= 0.8

    # 3+ гласных подряд
    if re.search(r"[aeiouy]{3,}", low):
        penalty *= 0.7

    return max(0.1, penalty)


def score(
        name: str,
        log_prob: Optional[float] = None,
        corpus: Optional[list] = None,
) -> dict:
    """
    Оценивает ник и возвращает словарь с оценками.

    Args:
        name: ник для оценки
        log_prob: log-prob под N-gram моделью (если есть)
        corpus: список ников корпуса (для оценки уникальности)
    """
    import math

    n = len(name)
    low = name.lower()

    # 1. Естественность
    if log_prob is not None:
        naturalness = 1.0 / (1.0 + math.exp(-log_prob - 2))
    else:
        naturalness = 0.5

    # 2-6. Фонетические критерии
    pron = pronounceability(name)
    balance = vowel_balance(name)
    length = length_score(name)
    killfeed = kill_feed_bonus(name)
    opening = open_ending(name)

    # 7. Уникальность
    if corpus:
        corpus_low = {c.lower() for c in corpus}
        if low in corpus_low:
            uniqueness = 0.0  # точная копия
        else:
            # Считаем общие биграммы
            from collections import Counter
            def bigrams(s):
                s = f"^{s}$"
                return Counter(s[i:i + 2] for i in range(len(s) - 1))

            name_bg = bigrams(low)
            corpus_bg = Counter()
            for c in list(corpus_low)[:100]:  # берём первые 100 для скорости
                corpus_bg.update(bigrams(c))

            common = sum((name_bg & corpus_bg).values())
            total = sum(name_bg.values()) or 1
            overlap = common / total
            uniqueness = 1.0 - overlap * 0.5  # штраф до 50% за совпадения
    else:
        uniqueness = 0.7

    # Базовый score
    base = (
            naturalness * WEIGHTS["naturalness"] +
            pron * WEIGHTS["pronounceability"] +
            balance * WEIGHTS["balance"] +
            length * WEIGHTS["length"] +
            killfeed * WEIGHTS["killfeed"] +
            opening * WEIGHTS["opening"] +
            uniqueness * WEIGHTS["uniqueness"]
    )

    # Штрафы
    penalty = compute_penalty(name)
    total = base * penalty

    return {
        "name": name,
        "score": round(total, 4),
        "naturalness": round(naturalness, 3),
        "pronounceability": round(pron, 3),
        "balance": round(balance, 3),
        "length": round(length, 3),
        "killfeed": round(killfeed, 3),
        "opening": round(opening, 3),
        "uniqueness": round(uniqueness, 3),
        "penalty": round(penalty, 3),
    }
