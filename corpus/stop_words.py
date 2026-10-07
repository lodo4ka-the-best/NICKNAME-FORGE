"""
Запрещённые слова и паттерны.

Используется в скорере и валидаторе, чтобы отсеивать:
  - служебные ники (admin, moderator)
  - мусорные паттерны (xXx_..._xXx, Shadow473)
"""

# Слова, которые нельзя использовать в никах
STOP_WORDS = {
    "admin", "moderator", "mod", "official", "support",
    "system", "root", "null", "undefined", "none",
    "test", "demo", "example", "sample",
    "user", "player", "guest", "anonymous",
}

# Регулярные выражения для отсеивания мусора
BAD_PATTERNS = [
    r"xXx.*xXx",  # 2008 год
    r".*\d{3,}",  # 3+ цифры подряд
    r"(.)\1{3,}",  # 4+ одинаковых буквы
    r"^[0-9]",  # начинается с цифры
]


def is_stop_word(name: str) -> bool:
    """Проверяет, является ли ник стоп-словом."""
    return name.lower() in STOP_WORDS


def matches_bad_pattern(name: str) -> bool:
    """Проверяет, матчится ли ник под запрещённый паттерн."""
    import re
    for pattern in BAD_PATTERNS:
        if re.search(pattern, name, re.IGNORECASE):
            return True
    return False


def is_clean(name: str) -> bool:
    """
    Комплексная проверка: не стоп-слово и не матчится под паттерн.
    """
    return not is_stop_word(name) and not matches_bad_pattern(name)
