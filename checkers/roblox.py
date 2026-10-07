"""Проверка занятости ника в Roblox."""

from typing import Optional

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def check(nickname: str) -> Optional[bool]:
    """Проверяет ник в Roblox."""
    if not HAS_REQUESTS:
        return None
    try:
        r = requests.get(
            "https://users.roblox.com/v1/usernames/users",
            json={"usernames": [nickname], "excludeBannedUsers": False},
            timeout=5,
        )
        if r.status_code == 200:
            data = r.json()
            return not bool(data.get("data"))
    except Exception:
        pass
    return None
