"""
Модели данных проекта.

Содержит dataclass'ы для передачи данных между модулями.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Set


@dataclass
class Profile:
    """Настройки генерации никнеймов."""
    style: str = "epic"                    # стиль: epic/dark/cute/...
    platform: str = "default"              # платформа: xbox/psn/steam/...
    min_len: int = 4                       # минимальная длина
    max_len: int = 12                      # максимальная длина
    temperature: float = 0.85              # температура генерации
    quality_threshold: float = 0.60        # порог качества
    max_retries: int = 20                  # попыток на ник
    seed: Optional[int] = None             # сид для воспроизводимости
    occupied: Set[str] = field(default_factory=set)  # занятые ники


@dataclass
class Result:
    """Результат генерации одного ника."""
    name: str                              # сам никнейм
    score: float                           # общая оценка (0-1)
    naturalness: float = 0.0               # естественность
    pronounceability: float = 0.0          # произносимость
    balance: float = 0.0                   # баланс гласных
    is_free: Optional[bool] = None         # свободен ли ник
