"""
Проверка занятости ника через DuckDuckGo.

Почему DuckDuckGo:
  - НЕ банит за частые запросы (в отличие от Google)
  - НЕ требует API-ключей
  - Использует Bing-выдачу (те же результаты)
  - Работает из коробки

Логика:
  1. Ищем "{ник}" esports / game / twitch
  2. Если находим профиль на киберспорт-сайте — ник занят
  3. Если ничего — свободен
"""

import time
from typing import Optional, List, Dict

try:
    from duckduckgo_search import DDGS
    HAS_DDG = True
except ImportError:
    HAS_DDG = False


# Домены, которые сигнализируют о занятости ника
ESPORTS_DOMAINS = [
    "liquipedia.net",
    "hltv.org",
    "twitch.tv",
    "youtube.com",
    "twitter.com",
    "x.com",
    "steamcommunity.com",
    "op.gg",
    "dotabuff.com",
    "faceit.com",
    "vlr.gg",
    "esports.net",
    "esportsearnings.com",
    "tracker.gg",
]

# Соцсети — тоже признак занятости
SOCIAL_DOMAINS = [
    "twitter.com",
    "x.com",
    "instagram.com",
    "tiktok.com",
    "facebook.com",
    "reddit.com",
]


def check_ddg(nickname: str, game: str = "esports") -> Optional[bool]:
    """
    Проверяет ник через DuckDuckGo.

    Returns:
        True  — свободен
        False — занят
        None  — не удалось проверить
    """
    if not HAS_DDG:
        return None

    query = f'"{nickname}" {game}'

    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=8))

        if not results:
            return True  # ничего не нашли — свободен

        # Проверяем домены
        all_urls = [r.get("href", "").lower() for r in results]

        for url in all_urls:
            if any(domain in url for domain in ESPORTS_DOMAINS):
                return False
            if any(domain in url for domain in SOCIAL_DOMAINS):
                return False

        # Если результаты есть, но не про игрока — тоже считаем занятым,
        # потому что ник уже где-то используется
        return False

    except Exception as e:
        print(f"  ⚠️ Ошибка DDG: {e}")
        return None


def check_ddg_batch(
    nicknames: List[str],
    game: str = "esports",
    delay: float = 1.5,
) -> List[Dict]:
    """
    Проверяет список ников через DuckDuckGo.

    Args:
        nicknames: список ников
        game: игра (esports/dota/csgo/valorant/lol)
        delay: пауза между запросами (сек)

    Returns:
        Список словарей с результатами
    """
    results = []

    for i, nick in enumerate(nicknames):
        is_free = check_ddg(nick, game)

        results.append({
            "nickname": nick,
            "is_free": is_free,
            "status": (
                "свободен" if is_free is True
                else "занят" if is_free is False
                else "неизвестно"
            ),
            "source": "duckduckgo",
        })

        if i < len(nicknames) - 1:
            time.sleep(delay)

    return results


if __name__ == "__main__":
    # Тест
    for nick in ["Kael", "s1mple", "XyzAbcNope123", "Draven"]:
        result = check_ddg(nick)
        mark = "✅" if result is True else "❌" if result is False else "❓"
        print(f"  {mark} {nick:<20} {result}")