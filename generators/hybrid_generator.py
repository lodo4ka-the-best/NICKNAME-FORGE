"""
Гибридный генератор: N-gram + Ollama.

Использует оба подхода:
  1. N-gram генерирует много кандидатов
  2. LLM выбирает лучшие
"""

from .ngram_generator import NGramModel
from .ollama_generator import OllamaGenerator


class HybridGenerator:
    """Гибрид N-gram и LLM."""

    def __init__(self):
        self.ngram = NGramModel()
        self.ollama = OllamaGenerator()

    def generate(self, style: str, count: int = 10) -> list:
        """Генерирует ники через оба подхода."""
        # TODO: реализовать гибрид
        return []
