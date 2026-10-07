"""
Корпус реальных ников для обучения модели.

Источники:
  - Киберспорт (CS:GO, Dota 2, LoL, Valorant)
  - Стримеры (Twitch)
  - Классические игровые ники

Каждый стиль имеет свой набор ников. Модель учится на них
и генерирует похожие.
"""

CORPUS = {
    # ─── EPIC — мощные, эпичные ───
    "epic": [
        # Киберспорт
        "s1mple", "ZywOo", "dev1ce", "NiKo", "b1t", "electroNic",
        "Kratos", "Ares", "Titan", "Rex", "Zane", "Kane",
        # Классика
        "Kael", "Draven", "Kraven", "Draxel", "Kaelor",
        "Zaron", "Grimar", "Tharen", "Vokar", "Raxen",
        "Draxus", "Korgan", "Vorn", "Malek", "Thok",
        "Krug", "Voren", "Kral", "Drak", "Zaru",
        "Korv", "Raxo", "Volk", "Grim", "Thar",
        "Dorn", "Krad", "Zorn", "Brak", "Thal",
        "Gorn", "Krax", "Drog", "Vrag", "Korg",
        "Vex", "Vok", "Rax", "Kor", "Drax",
        "Kraven", "Draxo", "Raxus", "Thares", "Aren",
        "Kaelin", "Dravin", "Kravin", "Raxin", "Draxin",
        "Kraven", "Draxel", "Kaelor", "Zaron", "Grimar",
    ],

    # ─── DARK — тёмные, мрачные ───
    "dark": [
        # Киберспорт
        "Nightfall", "Dusk", "Shade", "Wraith", "Void",
        # Классика
        "Nyx", "Vex", "Mor", "Nox", "Zul", "Sep",
        "Kha", "Vel", "Umbra", "Crypt", "Hex",
        "Morg", "Nyxo", "Vexar", "Zulth", "Sepp",
        "Khor", "Velk", "Nekr", "Morv", "Kalu",
        "Zeth", "Vokk", "Nokt", "Gloom", "Umbr",
        "Nocr", "Vant", "Morg", "Khol", "Xul",
        "Nyxar", "Vexin", "Morvex", "Zulmar", "Noktis",
        "Sepul", "Khalor", "Velgar", "Nyxen", "Vexis",
        "Umbrin", "Crypter", "Shaden", "Wraithen", "Voiden",
        "Duskar", "Nightar", "Shadowen", "Darkin", "Gloomir",
    ],

    # ─── CUTE — милые, мягкие ───
    "cute": [
        "Mochi", "Kiki", "Neko", "Puff", "Bun",
        "Mio", "Nana", "Pip", "Lulu", "Momo",
        "Nya", "Puf", "Koko", "Tofu", "Suki",
        "Mimi", "Boba", "Peko", "Yuki", "Momi",
        "Puni", "Loli", "Kuku", "Nunu", "Chibi",
        "Kiwi", "Miu", "Piyo", "Kuro", "Shiro",
        "Moka", "Kona", "Lumi", "Yumi", "Nini",
        "Popo", "Tutu", "Mochi", "Kiki", "Puff",
        "Neko", "Mimi", "Boba", "Momo", "Lulu",
        "Pip", "Nana", "Mio", "Nya", "Puf",
        "Koko", "Tofu", "Suki", "Miu", "Kuro",
    ],

    # ─── MAGE — магические, мистические ───
    "mage": [
        "Mira", "Lyra", "Sage", "Rune", "Nova",
        "Ael", "Ryn", "Sel", "Ith", "Arc",
        "Vor", "Lir", "Aeon", "Orin", "Eira",
        "Cael", "Ilya", "Solen", "Vael", "Thyr",
        "Sylv", "Myst", "Arka", "Lyr", "Eos",
        "Ira", "Sol", "Astra", "Aeth", "Elda",
        "Seer", "Oracle", "Rin", "Syl", "Theo",
        "Kael", "Vion", "Ely", "Aur", "Lux",
        "Mysta", "Runen", "Aelia", "Lyria", "Vaelin",
        "Sylin", "Arkan", "Rynar", "Ithir", "Selar",
        "Aethir", "Voriel", "Lirien", "Aeonir", "Noven",
    ],

    # ─── CYBER — технологичные, футуристичные ───
    "cyber": [
        "Neo", "Byte", "Flux", "Cipher", "Vector",
        "Nex", "Syn", "Vox", "Pix", "Zer",
        "Zap", "Chip", "Dot", "Kilo", "Nano",
        "Data", "Glitch", "Cryo", "Qbit", "Plex",
        "Vertex", "Zeta", "Onyx", "Nova", "Vex",
        "Nexo", "Hex", "Kode", "Zen", "Echo",
        "Nexor", "Synax", "Voxel", "Pixar", "Zerok",
        "Fluxen", "Chipen", "Dotex", "Kilon", "Nanox",
        "Datax", "Glitchen", "Cryon", "Qbiten", "Plexar",
        "Vertex", "Zetar", "Onyxen", "Novar", "Vexen",
        "Nexus", "Synth", "Vortex", "Pixel", "Zerox",
    ],

    # ─── SNIPER — точные, смертельные ───
    "sniper": [
        "Hawk", "Zero", "Ghost", "Falcon", "Strix",
        "Kest", "Vex", "Zan", "Kris", "Trek",
        "Skal", "Drak", "Sil", "Hunt", "Aim",
        "Shot", "Dead", "Echo", "Scope", "Raven",
        "Wraith", "Shade", "Talon", "Quick", "Swift",
        "Kestar", "Vexar", "Zanir", "Krisar", "Trekir",
        "Skalar", "Drakir", "Silen", "Hunter", "Aimer",
        "Shoten", "Deaden", "Echoen", "Scopen", "Ravenir",
        "Hawken", "Zeron", "Ghostir", "Falconir", "Strixen",
        "Talonir", "Quickir", "Swiftir", "Ravenar", "Shadowin",
    ],
}


def get_corpus(style: str) -> list:
    """
    Возвращает корпус для указанного стиля.
    Если стиль неизвестен — возвращает корпус epic.
    """
    return CORPUS.get(style, CORPUS["epic"])


def get_all_nicknames() -> list:
    """Возвращает все ники из всех стилей (для антидубликата)."""
    all_nicks = []
    for nicks in CORPUS.values():
        all_nicks.extend(nicks)
    return list(set(all_nicks))  # уникальные
