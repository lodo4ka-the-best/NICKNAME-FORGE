"""Интерфейс командной строки."""


def run():
    """Интерактивное меню."""
    print("=" * 60)
    print("  NICKNAME FORGE — CLI")
    print("=" * 60)
    style = input("Стиль (epic/dark/cute/...): ") or "epic"
    count = int(input("Сколько ников? [5]: ") or "5")
    print(f"Генерирую {count} ников в стиле {style}...")
    # TODO: вызвать генератор
