"""
Вспомогательные утилиты.
"""

import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict:
    """Загружает JSON-файл. Если файла нет — возвращает пустой словарь."""
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_json(data: Any, path: Path) -> None:
    """Сохраняет данные в JSON-файл."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def log(message: str, level: str = "info") -> None:
    """Простой лог с эмодзи."""
    icons = {
        "info": "ℹ️",
        "ok": "✅",
        "warn": "⚠️",
        "error": "❌",
    }
    print(f"{icons.get(level, "")} {message}")
