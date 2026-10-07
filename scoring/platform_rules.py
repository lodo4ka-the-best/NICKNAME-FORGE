"""
Правила платформ для валидации ников.
"""

import re
from core.constants import PLATFORM_RULES


def is_valid_for(name: str, platform: str) -> bool:
    """Проверяет ник по правилам платформы."""
    rules = PLATFORM_RULES.get(platform, PLATFORM_RULES["default"])

    if not (rules["min"] <= len(name) <= rules["max"]):
        return False

    if not re.match(rules["regex"], name):
        return False

    return True


def get_rules(platform: str) -> dict:
    """Возвращает правила платформы."""
    return PLATFORM_RULES.get(platform, PLATFORM_RULES["default"])


def describe(platform: str) -> str:
    """Человекочитаемое описание правил."""
    return get_rules(platform)["description"]
