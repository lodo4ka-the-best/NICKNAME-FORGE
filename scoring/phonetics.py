"""
Фонетические критерии оценки ников.

Все функции возвращают число от 0 до 1.
"""

import re

VOWELS = set("aeiouy")


def pronounceability(name: str) -> float:
    """
    Оценка произносимости через CV-паттерн.

    CV-паттерн: каждая согласная помечается C, гласная — V.
    Чем больше пар CV — тем лучше произносится.
    """
    letters = re.sub(r"[^a-z]", "", name.lower())
    if not letters:
        return 0.0

    cv = re.sub(r"[aeiouy]", "V", re.sub(r"[^aeiouy]", "C", letters))
    pairs = len(re.findall(r"CV", cv))
    return min(1.0, pairs / max(len(cv) / 2, 1))


def vowel_balance(name: str) -> float:
    """
    Баланс гласных.

    Оптимум — 40% гласных. Отклонение штрафуется.
    """
    letters = re.sub(r"[^a-z]", "", name.lower())
    if not letters:
        return 0.0

    v = sum(c in VOWELS for c in letters)
    ratio = v / len(letters)
    return max(0.0, 1.0 - abs(ratio - 0.4) * 2.5)


def open_ending(name: str) -> float:
    """
    Открытый финал.

    Ники, заканчивающиеся на гласную, читаются лучше.
    """
    if not name:
        return 0.0
    return 1.0 if name.lower()[-1] in VOWELS else 0.7


def kill_feed_bonus(name: str) -> float:
    """
    Kill Feed Test.

    Исследование Queen Mary University: ники на A-M
    воспринимаются как более успешные (alphabetical discrimination).
    """
    if not name:
        return 0.0
    return 1.0 if name[0].lower() in "abcdefghijklm" else 0.6


def length_score(name: str) -> float:
    """
    Оценка длины.

    Идеал — 4-7 символов. Дальше штраф.
    """
    n = len(name)
    if 4 <= n <= 7:
        return 1.0
    elif n == 8:
        return 0.7
    elif n == 9:
        return 0.4
    else:
        return 0.2
