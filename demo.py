"""
Демонстрация NICKNAME FORGE.

Запускает все стили по очереди и показывает результаты.
"""

from core.data_models import Profile
from interfaces.cli import CLI


def demo_style(style: str, count: int = 5):
    """Показать генерацию в одном стиле."""
    print()
    print("=" * 60)
    print(f"  ДЕМО: стиль {style.upper()}")
    print("=" * 60)

    profile = Profile(
        style=style,
        quality_threshold=0.60,
        max_retries=20,
        seed=42,
    )

    cli = CLI(profile)
    results = cli.generate(count)

    if not results:
        print("  ❌ Не удалось сгенерировать")
        return

    for i, r in enumerate(results, 1):
        bar = "█" * int(r.score * 14)
        print(f"  {i:>2}. {r.name:<12} {r.score:.3f}  {bar}")


def main():
    """Главная функция."""
    print("=" * 60)
    print("  NICKNAME FORGE — ДЕМОНСТРАЦИЯ")
    print("=" * 60)

    for style in ["epic", "dark", "cute", "mage", "cyber", "sniper"]:
        demo_style(style, count=5)

    print()
    print("=" * 60)
    print("  ГОТОВО")
    print("=" * 60)


if __name__ == "__main__":
    main()