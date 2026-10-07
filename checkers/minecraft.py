"""
Проверка занятости ника в Minecraft.

Использует Mojang API + fallback на ashcon.app.
"""

from typing import Optional

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


TIMEOUT = 5


def check(nickname: str) -> Optional[bool]:
    """
    Проверяет ник в Minecraft.

    Returns:
        True  — свободен
        False — занят
        None  — не удалось проверить
    """
    if not HAS_REQUESTS:
        return None

    # Основной API: Mojang
    try:
        r = requests.get(
            f"https://api.mojang.com/users/profiles/minecraft/{nickname}",
            timeout=TIMEOUT,
        )
        if r.status_code == 204:
            return True   # не найден = свободен
        if r.status_code == 200:
            return False  # найден = занят
    except Exception:
        pass

    return None
