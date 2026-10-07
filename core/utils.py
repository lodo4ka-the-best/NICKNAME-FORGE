"""
Вспомогательные утилиты.

  - load_json / save_json — работа с кэшем
  - log — красивый вывод в консоль
"""

import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict:
    """
    Загружает JSON-файл.
    Если файла нет или он битый — возвращает пустой словарь.
    """
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_json(data: Any, path: Path) -> None:
    """
    Сохраняет данные в JSON-файл.
    Создаёт родительские папки автоматически.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def log(message: str, level: str = "info") -> None:
    """
    Простой лог с эмодзи.

    Уровни: info, ok, warn, error
    """
    icons = {
        "info": "ℹ️",
        "ok": "✅",
        "warn": "⚠️",
        "error": "❌",
    }
    print(f"{icons.get(level, '')} {message}")
