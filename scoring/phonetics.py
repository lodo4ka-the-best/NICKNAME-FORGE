"""Фонетические критерии оценки ников."""

import re

VOWELS = set("aeiouy")


def pronounceability(name: str) -> float:
    """Оценка произносимости через CV-паттерн (0-1)."""
    letters = re.sub(r"[^a-z]", "", name.lower())
    if not letters:
        return 0.0
    cv = re.sub(r"[aeiouy]", "V", re.sub(r"[^aeiouy]", "C", letters))
    pairs = len(re.findall(r"CV", cv))
    return min(1.0, pairs / max(len(cv) / 2, 1))


def vowel_balance(name: str) -> float:
    """Баланс гласных (оптимум 40%)."""
    letters = re.sub(r"[^a-z]", "", name.lower())
    if not letters:
        return 0.0
    v = sum(c in VOWELS for c in letters)
    ratio = v / len(letters)
    return max(0.0, 1.0 - abs(ratio - 0.4) * 2.5)


def open_ending(name: str) -> float:
    """Открытый финал (на гласную)."""
    return 1.0 if name.lower()[-1] in VOWELS else 0.7
