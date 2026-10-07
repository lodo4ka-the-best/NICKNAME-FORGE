"""
Генератор ников через Ollama (локальная LLM).

Использует модель qwen3:4b или похожую для генерации
никнеймов по запросу пользователя.
"""

from typing import List

try:
    from ollama import chat
    HAS_OLLAMA = True
except ImportError:
    HAS_OLLAMA = False


class OllamaGenerator:
    """Генератор через локальную LLM."""

    def __init__(self, model: str = "qwen3:4b"):
        """
        Args:
            model: имя модели в Ollama
        """
        self.model = model

    def generate(self, style: str, count: int = 10) -> List[str]:
        """Генерирует ники через LLM."""
        if not HAS_OLLAMA:
            raise RuntimeError("Ollama не установлен. pip install ollama")
        # TODO: реализовать вызов LLM
        return []
