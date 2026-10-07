"""
Модели данных проекта.

Dataclass'ы для передачи данных между модулями.
Используются как "контейнеры" — без логики, только поля.
"""

from dataclasses import dataclass, field
from typing import Optional, Set


@dataclass
class Profile:
    """
    Настройки генерации никнеймов.

    Атрибуты:
        style: стиль ника (epic/dark/cute/mage/cyber/sniper)
        platform: платформа (xbox/psn/steam/minecraft/discord/default)
        min_len: минимальная длина ника
        max_len: максимальная длина ника
        temperature: температура генерации (0.6-1.2)
        quality_threshold: минимальный score (0-1)
        max_retries: сколько раз пробовать на один ник
        seed: сид для воспроизводимости
        occupied: множество занятых ников (чтобы не дублировать)
    """
    style: str = "epic"
    platform: str = "default"
    min_len: int = 4
    max_len: int = 12
    temperature: float = 0.85
    quality_threshold: float = 0.60
    max_retries: int = 20
    seed: Optional[int] = None
    occupied: Set[str] = field(default_factory=set)


@dataclass
class Result:
    """
    Результат генерации одного ника.

    Атрибуты:
        name: сам никнейм
        score: общая оценка (0-1)
        naturalness: естественность под моделью (0-1)
        pronounceability: произносимость (0-1)
        balance: баланс гласных (0-1)
        is_free: свободен ли ник (True/False/None)
    """
    name: str
    score: float
    naturalness: float = 0.0
    pronounceability: float = 0.0
    balance: float = 0.0
    is_free: Optional[bool] = None
    platform: Optional[str] = None

    def __str__(self) -> str:
        """Красивый вывод для print."""
        free_mark = (
            "✅" if self.is_free is True
            else "❌" if self.is_free is False
            else "❓"
        )
        return f"{self.name:<12} {self.score:.3f}  {free_mark}"
