"""Проверка занятости ника в Steam (заглушка)."""

from typing import Optional


def check(nickname: str, api_key: Optional[str] = None) -> Optional[bool]:
    """
    Проверяет ник в Steam.

    Steam не даёт публичного API для проверки доступности ника.
    Можно через Steam Web API с ключом, но это опционально.
    """
    # TODO: реализовать через Steam Web API с ключом
    return None