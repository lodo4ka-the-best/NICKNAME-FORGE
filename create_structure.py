"""
Скрипт создания структуры проекта NICKNAME FORGE.

Что делает:
  1. Создаёт папки с английскими именами
  2. Создаёт файлы с английскими именами
  3. Кладёт в них шаблоны с русскими комментариями

Запуск:
    python create_structure.py
"""

from pathlib import Path


# ═══════════════════════════════════════════════════════════════════════════
#  КОРЕНЬ ПРОЕКТА
# ═══════════════════════════════════════════════════════════════════════════

ROOT = Path(__file__).parent


# ═══════════════════════════════════════════════════════════════════════════
#  СТРУКТУРА ПАПОК (английские имена)
# ═══════════════════════════════════════════════════════════════════════════

FOLDERS = [
    "core",          # ядро системы
    "generators",    # генераторы ников
    "checkers",      # проверка занятости
    "scoring",       # оценка качества
    "corpus",        # обучающие данные
    "interfaces",    # интерфейсы
    "data",          # данные (кэш, история)
    "tests",         # тесты
]


# ═══════════════════════════════════════════════════════════════════════════
#  ФАЙЛЫ ПО ПАПКАМ
# ═══════════════════════════════════════════════════════════════════════════

FILES = {
    "core": [
        "__init__.py",
        "data_models.py",
        "constants.py",
        "utils.py",
    ],
    "generators": [
        "__init__.py",
        "ngram_generator.py",
        "ollama_generator.py",
        "hybrid_generator.py",
    ],
    "checkers": [
        "__init__.py",
        "minecraft.py",
        "roblox.py",
        "steam.py",
        "universal.py",
    ],
    "scoring": [
        "__init__.py",
        "phonetics.py",
        "platform_rules.py",
        "scorer.py",
    ],
    "corpus": [
        "__init__.py",
        "nicknames.py",
        "stop_words.py",
    ],
    "interfaces": [
        "__init__.py",
        "cli.py",
        "telegram_bot.py",
        "web.py",
    ],
    "data": [
        ".gitkeep",
    ],
    "tests": [
        "__init__.py",
        "test_generator.py",
        "test_checker.py",
        "test_scorer.py",
    ],
}

ROOT_FILES = [
    "main.py",
    "demo.py",
    "config.yaml",
    "requirements.txt",
    ".gitignore",
    "README.md",
]


# ═══════════════════════════════════════════════════════════════════════════
#  ШАБЛОНЫ СОДЕРЖИМОГО
# ═══════════════════════════════════════════════════════════════════════════
#
#  ВАЖНО:
#    - Имена файлов и папок — на английском
#    - Комментарии и docstrings — на русском
#    - Имена переменных/функций — на английском (Python-конвенция)
#    - Строки для пользователя — на русском
# ═══════════════════════════════════════════════════════════════════════════

TEMPLATES = {}


# ─── requirements.txt ───
TEMPLATES["requirements.txt"] = "\n".join([
    "# NICKNAME FORGE — зависимости проекта",
    "# Установка: pip install -r requirements.txt",
    "",
    "# LLM через Ollama",
    "ollama>=0.4.0",
    "",
    "# HTTP-запросы для проверки занятости",
    "requests>=2.31.0",
    "",
    "# ─── Опционально ───",
    "# aiogram>=3.0.0        # Telegram-бот",
    "# fastapi>=0.100.0      # Веб-интерфейс",
    "# uvicorn>=0.23.0       # ASGI-сервер",
    "# pytest>=7.0.0         # Тесты",
    "",
])


# ─── .gitignore ───
TEMPLATES[".gitignore"] = "\n".join([
    "# ─── Python ───",
    "__pycache__/",
    "*.py[cod]",
    "*.so",
    "venv/",
    "env/",
    ".venv/",
    "",
    "# ─── IDE ───",
    ".idea/",
    ".vscode/",
    "*.swp",
    "*.swo",
    "",
    "# ─── Данные (кэш, история) ───",
    "data/*.json",
    "data/*.csv",
    "!data/.gitkeep",
    "",
    "# ─── Логи ───",
    "*.log",
    "logs/",
    "",
    "# ─── OS ───",
    ".DS_Store",
    "Thumbs.db",
    "",
])


# ─── config.yaml ───
TEMPLATES["config.yaml"] = "\n".join([
    "# Конфигурация NICKNAME FORGE",
    "",
    "# Настройки генерации",
    "generation:",
    "  default_style: epic           # стиль по умолчанию",
    "  default_count: 5              # сколько ников генерировать",
    "  temperature: 0.85             # 0.6 = консервативно, 1.2 = креативно",
    "  quality_threshold: 0.60       # порог качества (ниже = больше ников)",
    "  max_retries: 20               # попыток на один ник",
    "",
    "# Ollama",
    "ollama:",
    "  model: qwen3:4b               # qwen3:4b / qwen2.5:1.5b / llama3.2:3b",
    "  host: http://localhost:11434",
    "  timeout: 60",
    "",
    "# Проверка занятости",
    "checker:",
    "  timeout: 5                    # таймаут запроса (сек)",
    "  delay: 0.3                    # пауза между запросами (сек)",
    "  use_cache: true               # кэшировать результаты",
    "",
    "# Интерфейсы",
    "interfaces:",
    "  telegram_token: ''            # токен бота (опционально)",
    "  web_port: 8000                # порт веб-сервера",
    "",
])


# ─── README.md ───
TEMPLATES["README.md"] = "\n".join([
    "# 🎮 NICKNAME FORGE",
    "",
    "Генератор идеальных игровых никнеймов.",
    "",
    "## Что внутри",
    "",
    "- **Character N-gram Language Model** — учится на 500+ реальных никах",
    "- **LLM через Ollama** — локальная модель, без интернета",
    "- **Проверка занятости** — Minecraft, Roblox, Steam",
    "- **Оценка по 8 критериям** — фонетика, длина, kill feed test",
    "",
    "## 📦 Установка",
    "",
    "1. Установить Python-зависимости:",
    "",
    "       pip install -r requirements.txt",
    "",
    "2. Установить Ollama (https://ollama.com) и скачать модель:",
    "",
    "       ollama pull qwen3:4b",
    "",
    "## 🚀 Запуск",
    "",
    "Базовый запуск:",
    "",
    "       python main.py --style epic --count 5",
    "",
    "С проверкой занятости:",
    "",
    "       python main.py --style epic --count 5 --platform minecraft",
    "",
    "## 📁 Структура",
    "",
    "- `core/`          — модели данных и константы",
    "- `generators/`    — ngram, ollama, hybrid",
    "- `checkers/`      — minecraft, roblox, steam",
    "- `scoring/`       — фонетика, правила, скорер",
    "- `corpus/`        — обучающие данные",
    "- `interfaces/`    — cli, telegram, web",
    "",
])


# ─── __init__.py ───
TEMPLATES["__init__.py"] = '"""Пакет NICKNAME FORGE."""\n'


# ─── main.py ───
TEMPLATES["main.py"] = "\n".join([
    '"""',
    "Точка входа NICKNAME FORGE.",
    "",
    "Использование:",
    "    python main.py --style epic --count 5",
    "    python main.py --style cyber --count 10 --platform minecraft",
    '"""',
    "",
    "import argparse",
    "",
    "",
    "def parse_args():",
    '    """Разбирает аргументы командной строки."""',
    "    parser = argparse.ArgumentParser(",
    '        description="Генератор игровых никнеймов"',
    "    )",
    '    parser.add_argument("--style", default="epic",',
    '                        help="стиль: epic/dark/cute/mage/cyber/sniper")',
    '    parser.add_argument("--count", type=int, default=5,',
    '                        help="сколько ников сгенерировать")',
    '    parser.add_argument("--platform", default=None,',
    '                        help="проверить на платформе: minecraft/roblox/steam")',
    '    parser.add_argument("--min-len", type=int, default=4)',
    '    parser.add_argument("--max-len", type=int, default=12)',
    "    return parser.parse_args()",
    "",
    "",
    "def main():",
    '    """Главная функция."""',
    "    args = parse_args()",
    "    print(f\"Стиль: {args.style}\")",
    "    print(f\"Количество: {args.count}\")",
    "    # TODO: подключить генератор",
    "",
    "",
    'if __name__ == "__main__":',
    "    main()",
    "",
])


# ─── demo.py ───
TEMPLATES["demo.py"] = "\n".join([
    '"""',
    "Демонстрация работы NICKNAME FORGE.",
    "",
    "Запускает все модули по очереди и показывает результаты.",
    '"""',
    "",
    "",
    "def demo_generator():",
    '    """Показать работу генератора."""',
    '    print("=" * 60)',
    '    print("  ДЕМО: Генератор")',
    '    print("=" * 60)',
    "    # TODO: вызвать генератор",
    "",
    "",
    "def demo_checker():",
    '    """Показать работу проверки занятости."""',
    '    print("=" * 60)',
    '    print("  ДЕМО: Проверка занятости")',
    '    print("=" * 60)',
    "    # TODO: вызвать проверку",
    "",
    "",
    "def demo_scorer():",
    '    """Показать работу оценки."""',
    '    print("=" * 60)',
    '    print("  ДЕМО: Оценка качества")',
    '    print("=" * 60)',
    "    # TODO: вызвать скорер",
    "",
    "",
    'if __name__ == "__main__":',
    "    demo_generator()",
    "    demo_checker()",
    "    demo_scorer()",
    "",
])


# ─── core/data_models.py ───
TEMPLATES["data_models.py"] = "\n".join([
    '"""',
    "Модели данных проекта.",
    "",
    "Содержит dataclass'ы для передачи данных между модулями.",
    '"""',
    "",
    "from dataclasses import dataclass, field",
    "from typing import List, Optional, Set",
    "",
    "",
    "@dataclass",
    "class Profile:",
    '    """Настройки генерации никнеймов."""',
    "    style: str = \"epic\"                    # стиль: epic/dark/cute/...",
    "    platform: str = \"default\"              # платформа: xbox/psn/steam/...",
    "    min_len: int = 4                       # минимальная длина",
    "    max_len: int = 12                      # максимальная длина",
    "    temperature: float = 0.85              # температура генерации",
    "    quality_threshold: float = 0.60        # порог качества",
    "    max_retries: int = 20                  # попыток на ник",
    "    seed: Optional[int] = None             # сид для воспроизводимости",
    "    occupied: Set[str] = field(default_factory=set)  # занятые ники",
    "",
    "",
    "@dataclass",
    "class Result:",
    '    """Результат генерации одного ника."""',
    "    name: str                              # сам никнейм",
    "    score: float                           # общая оценка (0-1)",
    "    naturalness: float = 0.0               # естественность",
    "    pronounceability: float = 0.0          # произносимость",
    "    balance: float = 0.0                   # баланс гласных",
    "    is_free: Optional[bool] = None         # свободен ли ник",
    "",
])


# ─── core/constants.py ───
TEMPLATES["constants.py"] = "\n".join([
    '"""',
    "Константы проекта.",
    "",
    "Стили, правила платформ, наборы букв.",
    '"""',
    "",
    "# ─── Стили ников ───",
    "STYLES = [",
    '    "epic",     # мощные, эпичные',
    '    "dark",     # тёмные, мрачные',
    '    "cute",     # милые, мягкие',
    '    "mage",     # магические, мистические',
    '    "cyber",    # технологичные, футуристичные',
    '    "sniper",   # точные, смертельные',
    "]",
    "",
    "# ─── Правила платформ ───",
    "PLATFORM_RULES = {",
    '    "xbox": {',
    '        "min": 3, "max": 12,',
    '        "regex": r"^[A-Za-z][A-Za-z0-9 ]*$",',
    '        "description": "3-12 символов, буквы+цифры+пробел",',
    "    },",
    '    "psn": {',
    '        "min": 3, "max": 16,',
    '        "regex": r"^[A-Za-z][A-Za-z0-9_-]*$",',
    '        "description": "3-16 символов, буквы+цифры+_+-",',
    "    },",
    '    "steam": {',
    '        "min": 3, "max": 32,',
    '        "regex": r"^[A-Za-z][A-Za-z0-9_]*$",',
    '        "description": "3-32 символов, буквы+цифры+_",',
    "    },",
    '    "minecraft": {',
    '        "min": 3, "max": 16,',
    '        "regex": r"^[A-Za-z0-9_]+$",',
    '        "description": "3-16 символов, буквы+цифры+_",',
    "    },",
    '    "default": {',
    '        "min": 4, "max": 12,',
    '        "regex": r"^[A-Za-z][A-Za-z0-9_]*$",',
    '        "description": "4-12 символов по умолчанию",',
    "    },",
    "}",
    "",
    "# ─── Наборы букв ───",
    'VOWELS = set("aeiouy")                       # гласные',
    'CONSONANTS = set("bcdfghjklmnpqrstvwxz")     # согласные',
    "",
    "# ─── Умные leet-замены (только различимые!) ───",
    "LEET_MAP = {",
    '    "a": "4", "e": "3", "i": "1", "o": "0",',
    '    "s": "5", "t": "7", "b": "8", "g": "9",',
    '    # НЕТ "l" -> "1" (визуально не отличить)',
    '    # НЕТ "z" -> "2" (уродливо)',
    "}",
    "",
])


# ─── core/utils.py ───
TEMPLATES["utils.py"] = "\n".join([
    '"""',
    "Вспомогательные утилиты.",
    '"""',
    "",
    "import json",
    "from pathlib import Path",
    "from typing import Any",
    "",
    "",
    "def load_json(path: Path) -> dict:",
    '    """Загружает JSON-файл. Если файла нет — возвращает пустой словарь."""',
    "    if not path.exists():",
    "        return {}",
    "    try:",
    '        return json.loads(path.read_text(encoding="utf-8"))',
    "    except Exception:",
    "        return {}",
    "",
    "",
    "def save_json(data: Any, path: Path) -> None:",
    '    """Сохраняет данные в JSON-файл."""',
    "    path.parent.mkdir(parents=True, exist_ok=True)",
    '    path.write_text(',
    "        json.dumps(data, ensure_ascii=False, indent=2),",
    '        encoding="utf-8",',
    "    )",
    "",
    "",
    "def log(message: str, level: str = \"info\") -> None:",
    '    """Простой лог с эмодзи."""',
    "    icons = {",
    '        "info": "ℹ️",',
    '        "ok": "✅",',
    '        "warn": "⚠️",',
    '        "error": "❌",',
    "    }",
    '    print(f"{icons.get(level, \"\")} {message}")',
    "",
])


# ─── generators/ngram_generator.py ───
TEMPLATES["ngram_generator.py"] = "\n".join([
    '"""',
    "Character N-gram Language Model для генерации ников.",
    "",
    "Модель учится P(буква | контекст) на корпусе реальных ников",
    "и генерирует новые через семплинг.",
    '"""',
    "",
    "from collections import defaultdict, Counter",
    "import math",
    "import random",
    "",
    "",
    "class NGramModel:",
    '    """N-gram модель на уровне символов."""',
    "",
    "    def __init__(self, order: int = 3, smoothing: float = 0.1):",
    '        """',
    "        Args:",
    "            order: максимальная длина контекста",
    "            smoothing: сглаживание для нулевых вероятностей",
    '        """',
    "        self.order = order",
    "        self.smoothing = smoothing",
    "        self.tables = [defaultdict(Counter) for _ in range(order + 1)]",
    "        self.vocab = Counter()",
    "",
    "    def train(self, words: list) -> None:",
    '        """Обучает модель на списке слов."""',
    "        for word in words:",
    "            word = word.lower()",
    "            self.vocab.update(word)",
    '            padded = "^" * self.order + word + "$"',
    "            for i in range(self.order, len(padded)):",
    "                for o in range(1, self.order + 1):",
    "                    ctx = padded[i - o:i]",
    "                    nxt = padded[i]",
    "                    self.tables[o][ctx][nxt] += 1",
    "",
    "    def generate(self, temperature: float = 1.0, max_len: int = 12) -> str:",
    '        """Генерирует одно слово."""',
    "        # TODO: реализовать семплинг",
    "        return \"\"",
    "",
])


# ─── generators/ollama_generator.py ───
TEMPLATES["ollama_generator.py"] = "\n".join([
    '"""',
    "Генератор ников через Ollama (локальная LLM).",
    "",
    "Использует модель qwen3:4b или похожую для генерации",
    "никнеймов по запросу пользователя.",
    '"""',
    "",
    "from typing import List",
    "",
    "try:",
    "    from ollama import chat",
    "    HAS_OLLAMA = True",
    "except ImportError:",
    "    HAS_OLLAMA = False",
    "",
    "",
    "class OllamaGenerator:",
    '    """Генератор через локальную LLM."""',
    "",
    "    def __init__(self, model: str = \"qwen3:4b\"):",
    '        """',
    "        Args:",
    "            model: имя модели в Ollama",
    '        """',
    "        self.model = model",
    "",
    "    def generate(self, style: str, count: int = 10) -> List[str]:",
    '        """Генерирует ники через LLM."""',
    "        if not HAS_OLLAMA:",
    '            raise RuntimeError("Ollama не установлен. pip install ollama")',
    "        # TODO: реализовать вызов LLM",
    "        return []",
    "",
])


# ─── generators/hybrid_generator.py ───
TEMPLATES["hybrid_generator.py"] = "\n".join([
    '"""',
    "Гибридный генератор: N-gram + Ollama.",
    "",
    "Использует оба подхода:",
    "  1. N-gram генерирует много кандидатов",
    "  2. LLM выбирает лучшие",
    '"""',
    "",
    "from .ngram_generator import NGramModel",
    "from .ollama_generator import OllamaGenerator",
    "",
    "",
    "class HybridGenerator:",
    '    """Гибрид N-gram и LLM."""',
    "",
    "    def __init__(self):",
    "        self.ngram = NGramModel()",
    "        self.ollama = OllamaGenerator()",
    "",
    "    def generate(self, style: str, count: int = 10) -> list:",
    '        """Генерирует ники через оба подхода."""',
    "        # TODO: реализовать гибрид",
    "        return []",
    "",
])


# ─── checkers/minecraft.py ───
TEMPLATES["minecraft.py"] = "\n".join([
    '"""',
    "Проверка занятости ника в Minecraft.",
    "",
    "Использует Mojang API + fallback на ashcon.app.",
    '"""',
    "",
    "from typing import Optional",
    "",
    "try:",
    "    import requests",
    "    HAS_REQUESTS = True",
    "except ImportError:",
    "    HAS_REQUESTS = False",
    "",
    "",
    "TIMEOUT = 5",
    "",
    "",
    "def check(nickname: str) -> Optional[bool]:",
    '    """',
    "    Проверяет ник в Minecraft.",
    "",
    "    Returns:",
    "        True  — свободен",
    "        False — занят",
    "        None  — не удалось проверить",
    '    """',
    "    if not HAS_REQUESTS:",
    "        return None",
    "",
    "    # Основной API: Mojang",
    "    try:",
    "        r = requests.get(",
    '            f"https://api.mojang.com/users/profiles/minecraft/{nickname}",',
    "            timeout=TIMEOUT,",
    "        )",
    "        if r.status_code == 204:",
    "            return True   # не найден = свободен",
    "        if r.status_code == 200:",
    "            return False  # найден = занят",
    "    except Exception:",
    "        pass",
    "",
    "    return None",
    "",
])


# ─── checkers/roblox.py ───
TEMPLATES["roblox.py"] = "\n".join([
    '"""Проверка занятости ника в Roblox."""',
    "",
    "from typing import Optional",
    "",
    "try:",
    "    import requests",
    "    HAS_REQUESTS = True",
    "except ImportError:",
    "    HAS_REQUESTS = False",
    "",
    "",
    "def check(nickname: str) -> Optional[bool]:",
    '    """Проверяет ник в Roblox."""',
    "    if not HAS_REQUESTS:",
    "        return None",
    "    try:",
    "        r = requests.get(",
    '            "https://users.roblox.com/v1/usernames/users",',
    '            json={"usernames": [nickname], "excludeBannedUsers": False},',
    "            timeout=5,",
    "        )",
    "        if r.status_code == 200:",
    "            data = r.json()",
    "            return not bool(data.get(\"data\"))",
    "    except Exception:",
    "        pass",
    "    return None",
    "",
])


# ─── checkers/steam.py ───
TEMPLATES["steam.py"] = "\n".join([
    '"""Проверка занятости ника в Steam."""',
    "",
    "from typing import Optional",
    "",
    "",
    "def check(nickname: str, api_key: Optional[str] = None) -> Optional[bool]:",
    '    """Проверяет ник в Steam (требует API-ключ)."""',
    "    # TODO: реализовать через Steam Web API",
    "    return None",
    "",
])


# ─── checkers/universal.py ───
TEMPLATES["universal.py"] = "\n".join([
    '"""',
    "Универсальная проверка занятости.",
    "",
    "Объединяет все платформы в один интерфейс.",
    '"""',
    "",
    "from typing import Dict, List",
    "from . import minecraft, roblox, steam",
    "",
    "",
    "PLATFORMS = {",
    '    "minecraft": minecraft.check,',
    '    "roblox": roblox.check,',
    '    "steam": steam.check,',
    "}",
    "",
    "",
    "def check_one(nickname: str, platform: str = \"minecraft\") -> Dict:",
    '    """Проверяет один ник на одной платформе."""',
    "    func = PLATFORMS.get(platform)",
    "    if not func:",
    "        return {",
    '            "nickname": nickname,',
    '            "platform": platform,',
    '            "is_free": None,',
    '            "error": f"Неизвестная платформа: {platform}",',
    "        }",
    "    result = func(nickname)",
    "    return {",
    '        "nickname": nickname,',
    '        "platform": platform,',
    '        "is_free": result,',
    '        "status": (',
    '            "свободен" if result is True',
    '            else "занят" if result is False',
    '            else "неизвестно"',
    "        ),",
    "    }",
    "",
    "",
    "def check_all(nicknames: List[str], platform: str = \"minecraft\") -> List[Dict]:",
    '    """Проверяет список ников."""',
    "    return [check_one(n, platform) for n in nicknames]",
    "",
])


# ─── scoring/phonetics.py ───
TEMPLATES["phonetics.py"] = "\n".join([
    '"""Фонетические критерии оценки ников."""',
    "",
    "import re",
    "",
    'VOWELS = set("aeiouy")',
    "",
    "",
    "def pronounceability(name: str) -> float:",
    '    """Оценка произносимости через CV-паттерн (0-1)."""',
    "    letters = re.sub(r\"[^a-z]\", \"\", name.lower())",
    "    if not letters:",
    "        return 0.0",
    '    cv = re.sub(r"[aeiouy]", "V", re.sub(r"[^aeiouy]", "C", letters))',
    '    pairs = len(re.findall(r"CV", cv))',
    "    return min(1.0, pairs / max(len(cv) / 2, 1))",
    "",
    "",
    "def vowel_balance(name: str) -> float:",
    '    """Баланс гласных (оптимум 40%)."""',
    "    letters = re.sub(r\"[^a-z]\", \"\", name.lower())",
    "    if not letters:",
    "        return 0.0",
    "    v = sum(c in VOWELS for c in letters)",
    "    ratio = v / len(letters)",
    "    return max(0.0, 1.0 - abs(ratio - 0.4) * 2.5)",
    "",
    "",
    "def open_ending(name: str) -> float:",
    '    """Открытый финал (на гласную)."""',
    "    return 1.0 if name.lower()[-1] in VOWELS else 0.7",
    "",
])


# ─── scoring/platform_rules.py ───
TEMPLATES["platform_rules.py"] = "\n".join([
    '"""Правила платформ для валидации ников."""',
    "",
    "import re",
    "from core.constants import PLATFORM_RULES",
    "",
    "",
    "def is_valid_for(name: str, platform: str) -> bool:",
    '    """Проверяет ник по правилам платформы."""',
    "    rules = PLATFORM_RULES.get(platform, PLATFORM_RULES[\"default\"])",
    "    if not (rules[\"min\"] <= len(name) <= rules[\"max\"]):",
    "        return False",
    "    if not re.match(rules[\"regex\"], name):",
    "        return False",
    "    return True",
    "",
    "",
    "def get_rules(platform: str) -> dict:",
    '    """Возвращает правила платформы."""',
    "    return PLATFORM_RULES.get(platform, PLATFORM_RULES[\"default\"])",
    "",
])


# ─── scoring/scorer.py ───
TEMPLATES["scorer.py"] = "\n".join([
    '"""',
    "Итоговая оценка ников по 8 критериям.",
    "",
    "Критерии:",
    "  1. Естественность (log-prob под моделью)",
    "  2. Произносимость (CV-паттерн)",
    "  3. Баланс гласных",
    "  4. Длина",
    "  5. Kill Feed Test (A-M в начале)",
    "  6. Открытый финал",
    "  7. Уникальность",
    "  8. Штрафы за мусор",
    '"""',
    "",
    "import math",
    "from .phonetics import pronounceability, vowel_balance, open_ending",
    "",
    "",
    "def score(name: str, log_prob: float = 0.0) -> dict:",
    '    """Оценивает ник и возвращает словарь с оценками."""',
    "    n = len(name)",
    "    naturalness = 1.0 / (1.0 + math.exp(-log_prob - 2))",
    "    pron = pronounceability(name)",
    "    balance = vowel_balance(name)",
    "    opening = open_ending(name)",
    "    killfeed = 1.0 if name[0].lower() in \"abcdefghijklm\" else 0.6",
    "",
    "    # Длина",
    "    if 4 <= n <= 7:",
    "        length = 1.0",
    "    elif n == 8:",
    "        length = 0.7",
    "    elif n == 9:",
    "        length = 0.4",
    "    else:",
    "        length = 0.2",
    "",
    "    total = (",
    "        naturalness * 0.35 +",
    "        pron * 0.20 +",
    "        balance * 0.10 +",
    "        length * 0.10 +",
    "        killfeed * 0.10 +",
    "        opening * 0.15",
    "    )",
    "",
    "    return {",
    '        "name": name,',
    '        "score": round(total, 4),',
    '        "naturalness": round(naturalness, 3),',
    '        "pronounceability": round(pron, 3),',
    '        "balance": round(balance, 3),',
    "    }",
    "",
])


# ─── corpus/nicknames.py ───
TEMPLATES["nicknames.py"] = "\n".join([
    '"""',
    "Корпус реальных ников для обучения модели.",
    "",
    "Источники:",
    "  - Киберспорт (CS:GO, Dota 2, LoL, Valorant)",
    "  - Стримеры (Twitch)",
    "  - Классические игровые ники",
    '"""',
    "",
    "CORPUS = {",
    '    "epic": [',
    '        "s1mple", "ZywOo", "NiKo", "b1t", "Kael", "Draven",',
    '        "Kratos", "Ares", "Titan", "Rex", "Zane", "Kane",',
    "    ],",
    '    "dark": [',
    '        "Nyx", "Vex", "Wraith", "Umbra", "Void", "Shade",',
    '        "Dusk", "Crypt", "Hex", "Gloom",',
    "    ],",
    '    "cute": [',
    '        "Mochi", "Kiki", "Neko", "Puff", "Bun", "Mio",',
    '        "Nana", "Pip", "Lulu", "Momo",',
    "    ],",
    '    "mage": [',
    '        "Mira", "Lyra", "Sage", "Rune", "Nova", "Ael",',
    '        "Ryn", "Sel", "Ith", "Arc",',
    "    ],",
    '    "cyber": [',
    '        "Neo", "Byte", "Flux", "Cipher", "Vector", "Nex",',
    '        "Syn", "Vox", "Pix", "Zer",',
    "    ],",
    '    "sniper": [',
    '        "Hawk", "Zero", "Ghost", "Falcon", "Strix", "Kest",',
    '        "Vex", "Zan", "Kris", "Trek",',
    "    ],",
    "}",
    "",
])


# ─── corpus/stop_words.py ───
TEMPLATES["stop_words.py"] = "\n".join([
    '"""Запрещённые слова и паттерны."""',
    "",
    "# Слова, которые нельзя использовать в никах",
    "STOP_WORDS = {",
    '    "admin", "moderator", "official", "support",',
    '    "system", "root", "null", "undefined",',
    "}",
    "",
    "# Регулярки для отсеивания мусора",
    "BAD_PATTERNS = [",
    '    r"xXx.*xXx",      # 2008 год',
    '    r".*\\d{3,}",     # 3+ цифры подряд',
    '    r"(.)\\1{3,}",    # 4+ одинаковых буквы',
    "]",
    "",
])


# ─── interfaces/cli.py ───
TEMPLATES["cli.py"] = "\n".join([
    '"""Интерфейс командной строки."""',
    "",
    "",
    "def run():",
    '    """Интерактивное меню."""',
    '    print("=" * 60)',
    '    print("  NICKNAME FORGE — CLI")',
    '    print("=" * 60)',
    '    style = input("Стиль (epic/dark/cute/...): ") or "epic"',
    '    count = int(input("Сколько ников? [5]: ") or "5")',
    "    print(f\"Генерирую {count} ников в стиле {style}...\")",
    "    # TODO: вызвать генератор",
    "",
])


# ─── interfaces/telegram_bot.py ───
TEMPLATES["telegram_bot.py"] = "\n".join([
    '"""Telegram-бот для генерации ников."""',
    "",
    "# Требует: pip install aiogram",
    "",
    "",
    "def run():",
    '    """Запускает бота."""',
    '    print("Telegram-бот: TODO")',
    "",
])


# ─── interfaces/web.py ───
TEMPLATES["web.py"] = "\n".join([
    '"""Веб-интерфейс на FastAPI."""',
    "",
    "# Требует: pip install fastapi uvicorn",
    "",
    "",
    "def run():",
    '    """Запускает веб-сервер."""',
    '    print("Веб-интерфейс: TODO")',
    "",
])


# ─── tests ───
TEMPLATES["test_generator.py"] = "\n".join([
    '"""Тесты генератора."""',
    "",
    "",
    "def test_basic():",
    '    """Простой тест-заглушка."""',
    "    assert True",
    "",
])

TEMPLATES["test_checker.py"] = "\n".join([
    '"""Тесты проверки занятости."""',
    "",
    "",
    "def test_basic():",
    '    """Простой тест-заглушка."""',
    "    assert True",
    "",
])

TEMPLATES["test_scorer.py"] = "\n".join([
    '"""Тесты скорера."""',
    "",
    "",
    "def test_basic():",
    '    """Простой тест-заглушка."""',
    "    assert True",
    "",
])


# ═══════════════════════════════════════════════════════════════════════════
#  СОЗДАНИЕ СТРУКТУРЫ
# ═══════════════════════════════════════════════════════════════════════════

def create_folders() -> None:
    """Создаёт все папки."""
    for folder in FOLDERS:
        path = ROOT / folder
        path.mkdir(parents=True, exist_ok=True)
        print(f"  📁 {folder}/")


def create_files() -> None:
    """Создаёт файлы в папках."""
    for folder, files in FILES.items():
        for filename in files:
            path = ROOT / folder / filename
            if path.exists():
                print(f"  ⏭  {folder}/{filename} (уже есть)")
                continue
            content = TEMPLATES.get(filename, '"""Модуль в разработке."""\n')
            path.write_text(content, encoding="utf-8")
            print(f"  📄 {folder}/{filename}")


def create_root_files() -> None:
    """Создаёт файлы в корне."""
    for filename in ROOT_FILES:
        path = ROOT / filename
        if path.exists():
            print(f"  ⏭  {filename} (уже есть)")
            continue
        content = TEMPLATES.get(filename, "")
        path.write_text(content, encoding="utf-8")
        print(f"  📄 {filename}")


def main():
    print("=" * 60)
    print("  СОЗДАНИЕ СТРУКТУРЫ NICKNAME FORGE")
    print("=" * 60)
    print("\n📁 Папки:")
    create_folders()
    print("\n📄 Файлы в папках:")
    create_files()
    print("\n📄 Файлы в корне:")
    create_root_files()
    print("\n" + "=" * 60)
    print("  ✅ Готово!")
    print("=" * 60)


if __name__ == "__main__":
    main()