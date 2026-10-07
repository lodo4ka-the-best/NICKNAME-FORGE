"""
Универсальная проверка занятости.

Объединяет все платформы в один интерфейс.
"""

from typing import Dict, List
from . import minecraft, roblox, steam


PLATFORMS = {
    "minecraft": minecraft.check,
    "roblox": roblox.check,
    "steam": steam.check,
}


def check_one(nickname: str, platform: str = "minecraft") -> Dict:
    """Проверяет один ник на одной платформе."""
    func = PLATFORMS.get(platform)
    if not func:
        return {
            "nickname": nickname,
            "platform": platform,
            "is_free": None,
            "error": f"Неизвестная платформа: {platform}",
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


def check_all(nicknames: List[str], platform: str = "minecraft") -> List[Dict]:
    """Проверяет список ников."""
    return [check_one(n, platform) for n in nicknames]
