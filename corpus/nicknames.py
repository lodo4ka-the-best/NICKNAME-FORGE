"""
Корпус реальных ников для обучения модели.

Источники:
  - Киберспорт (CS:GO, Dota 2, LoL, Valorant)
  - Стримеры (Twitch)
  - Классические игровые ники
"""

CORPUS = {
    "epic": [
        "s1mple", "ZywOo", "NiKo", "b1t", "Kael", "Draven",
        "Kratos", "Ares", "Titan", "Rex", "Zane", "Kane",
    ],
    "dark": [
        "Nyx", "Vex", "Wraith", "Umbra", "Void", "Shade",
        "Dusk", "Crypt", "Hex", "Gloom",
    ],
    "cute": [
        "Mochi", "Kiki", "Neko", "Puff", "Bun", "Mio",
        "Nana", "Pip", "Lulu", "Momo",
    ],
    "mage": [
        "Mira", "Lyra", "Sage", "Rune", "Nova", "Ael",
        "Ryn", "Sel", "Ith", "Arc",
    ],
    "cyber": [
        "Neo", "Byte", "Flux", "Cipher", "Vector", "Nex",
        "Syn", "Vox", "Pix", "Zer",
    ],
    "sniper": [
        "Hawk", "Zero", "Ghost", "Falcon", "Strix", "Kest",
        "Vex", "Zan", "Kris", "Trek",
    ],
}
