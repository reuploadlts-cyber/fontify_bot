from bot.services.font_engine import convert_text
from bot.services.decor_engine import apply_decor, apply_wrapper


def combo_style(text: str, font: str, decor: str = None, wrapper: str = None):
    styled = convert_text(text, font)

    if decor:
        styled = apply_decor(styled, decor)

    if wrapper:
        styled = apply_wrapper(styled, wrapper)

    return styled
