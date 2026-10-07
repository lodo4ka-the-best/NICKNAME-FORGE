"""
Универсальная проверка занятости.

Объединяет все платформы в один интерфейс.
"""

import time
from typing import Dict, List

from . import minecraft, roblox, steam


# Регистрация платформ
PLATFORMS = {
    "minecraft": minecraft.check,
    "roblox": roblox.check,
    "steam": steam.check,
}

# Задержка между запросами (сек), чтобы не забанили
DELAY = 0.3


def check_one(nickname: str, platform: str = "minecraft") -> Dict:
    """
    Проверяет один ник на одной платформе.

    Returns:
        Словарь с полями: nickname, platform, is_free, status
    """
    func = PLATFORMS.get(platform)

    if not func:
        return {
            "nickname": nickname,
            "platform": platform,
            "is_free": None,
            "status": "неизвестная платформа",
        }

    result = func(nickname)

    return {
        "nickname": nickname,
        "platform": platform,
        "is_free": result,
        "status": (
            "свободен" if result is True
            else "занят" if result is False
            else "неизвестно"
        ),
    }


def check_all(
    nicknames: List[str],
    platform: str = "minecraft",
    delay: float = DELAY,
) -> List[Dict]:
    """
    Проверяет список ников.

    Args:
        nicknames: список ников
        platform: платформа
        delay: пауза между запросами (сек)
    """
    results = []
    for i, nick in enumerate(nicknames):
        results.append(check_one(nick, platform))
        if i < len(nicknames) - 1:
            time.sleep(delay)
    return results