import random


def random_hex_color() -> str:
    return f"#{random.randint(0, 0xFFFFFF):06x}".lower()
