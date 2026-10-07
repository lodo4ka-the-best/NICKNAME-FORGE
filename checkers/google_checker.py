"""
Проверка занятости ника через интернет (DuckDuckGo).

Логика:
  1. Ищем "{ник}" esports / game / twitch
  2. Если находим профиль на киберспорт-сайте — ник занят
  3. Если находим в соцсетях — ник занят
  4. Если ничего — свободен

Почему DuckDuckGo, а не Google:
  - Google банит скрейпинг (получаем 0 результатов)
  - DuckDuckGo работает стабильно
  - Не требует API-ключей
  - Использует Bing-выдачу (те же результаты)

Зависимость: pip install ddgs
"""

import time
from typing import Optional, List, Dict

try:
    from ddgs import DDGS

    HAS_DDGS = True
except ImportError:
    HAS_DDGS = False

# Домены, которые сигнализируют о занятости ника
ESPORTS_DOMAINS = [
    "liquipedia.net",  # главный источник киберспорта
    "hltv.org",  # CS:GO/CS2
    "twitch.tv",  # стримы
    "youtube.com",  # ютуб
    "steamcommunity.com",  # Steam
    "op.gg",  # LoL
    "dotabuff.com",  # Dota 2
    "faceit.com",  # CS2
    "vlr.gg",  # Valorant
    "esports.net",  # новости киберспорта
    "esportsearnings.com",  # призовые
    "tracker.gg",  # статистика
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


def check_google(nickname: str, game: str = "esports") -> Optional[bool]:
    """
    Проверяет ник через DuckDuckGo.

    Логика:
      1. Один запрос: "{ник} {игра}"
      2. Если результат есть и ник упомянут в title/url/body — занят
      3. Если ничего — свободен
    """
    if not HAS_DDGS:
        return None

    query = f"{nickname} {game}"
    nick_lower = nickname.lower()

    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=10))
    except Exception as e:
        if "No results found" in str(e):
            return True  # ничего не нашли — свободен
        print(f"  ⚠️ Ошибка DDG для '{nickname}': {e}")
        return None

    if not results:
        return True

    for r in results:
        url = (r.get("href") or "").lower()
        title = (r.get("title") or "").lower()
        body = (r.get("body") or "").lower()

        # Ник должен быть хотя бы в одном поле
        if not (nick_lower in title or nick_lower in url or nick_lower in body):
            continue

        # Ник найден — куда ведёт?
        if any(d in url for d in ESPORTS_DOMAINS):
            return False
        if any(d in url for d in SOCIAL_DOMAINS):
            return False
        return False  # упомянут где-то ещё = тоже занят

    return True


def check_google_batch(
        nicknames: List[str],
        game: str = "esports",
        delay: float = 1.5,
) -> List[Dict]:
    """
    Проверяет список ников через DuckDuckGo.

    Args:
        nicknames: список ников
        game: контекст поиска
        delay: пауза между запросами (сек)

    Returns:
        Список словарей с результатами
    """
    results = []

    for i, nick in enumerate(nicknames):
        is_free = check_google(nick, game)

        results.append({
            "nickname": nick,
            "is_free": is_free,
            "status": (
                "свободен" if is_free is True
                else "занят" if is_free is False
                else "неизвестно"
            ),
            "source": "ddgs",
        })

        if i < len(nicknames) - 1:
            time.sleep(delay)

    return results


# ─── Тест при прямом запуске ───
if __name__ == "__main__":
    print("=" * 60)
    print("  ТЕСТ ПРОВЕРКИ ЧЕРЕЗ DUCKDUCKGO")
    print("=" * 60)

    test_nicks = ["Kael", "s1mple", "Draven", "XyzAbcNope123"]

    for nick in test_nicks:
        result = check_google(nick)
        mark = (
            "✅ свободен" if result is True
            else "❌ занят" if result is False
            else "❓ неизвестно"
        )
        print(f"  {nick:<20} {mark}")
