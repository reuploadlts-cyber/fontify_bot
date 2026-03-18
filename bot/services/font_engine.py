# Font conversion engine

def apply_font(text: str, font_map: dict) -> str:
    result = ""

    for char in text:
        lower_char = char.lower()

        if lower_char in font_map:
            styled_char = font_map[lower_char]

            # Preserve uppercase if needed
            if char.isupper():
                result += styled_char.upper()
            else:
                result += styled_char
        else:
            result += char

    return result


# ------------------ FONT MAPS ------------------

bold_map = {
    "a": "𝗮", "b": "𝗯", "c": "𝗰", "d": "𝗱", "e": "𝗲",
    "f": "𝗳", "g": "𝗴", "h": "𝗵", "i": "𝗶", "j": "𝗷",
    "k": "𝗸", "l": "𝗹", "m": "𝗺", "n": "𝗻", "o": "𝗼",
    "p": "𝗽", "q": "𝗾", "r": "𝗿", "s": "𝘀", "t": "𝘁",
    "u": "𝘂", "v": "𝘃", "w": "𝘄", "x": "𝘅", "y": "𝘆",
    "z": "𝘇"
}

italic_map = {
    "a": "𝘢", "b": "𝘣", "c": "𝘤", "d": "𝘥", "e": "𝘦",
    "f": "𝘧", "g": "𝘨", "h": "𝘩", "i": "𝘪", "j": "𝘫",
    "k": "𝘬", "l": "𝘭", "m": "𝘮", "n": "𝘯", "o": "𝘰",
    "p": "𝘱", "q": "𝘲", "r": "𝘳", "s": "𝘴", "t": "𝘵",
    "u": "𝘶", "v": "𝘷", "w": "𝘸", "x": "𝘹", "y": "𝘺",
    "z": "𝘻"
}

mono_map = {
    "a": "𝚊", "b": "𝚋", "c": "𝚌", "d": "𝚍", "e": "𝚎",
    "f": "𝚏", "g": "𝚐", "h": "𝚑", "i": "𝚒", "j": "𝚓",
    "k": "𝚔", "l": "𝚕", "m": "𝚖", "n": "𝚗", "o": "𝚘",
    "p": "𝚙", "q": "𝚚", "r": "𝚛", "s": "𝚜", "t": "𝚝",
    "u": "𝚞", "v": "𝚟", "w": "𝚠", "x": "𝚡", "y": "𝚢",
    "z": "𝚣"
}

double_map = {
    "a": "𝕒", "b": "𝕓", "c": "𝕔", "d": "𝕕", "e": "𝕖",
    "f": "𝕗", "g": "𝕘", "h": "𝕙", "i": "𝕚", "j": "𝕛",
    "k": "𝕜", "l": "𝕝", "m": "𝕞", "n": "𝕟", "o": "𝕠",
    "p": "𝕡", "q": "𝕢", "r": "𝕣", "s": "𝕤", "t": "𝕥",
    "u": "𝕦", "v": "𝕧", "w": "𝕨", "x": "𝕩", "y": "𝕪",
    "z": "𝕫"
}

small_caps_map = {
    "a": "ᴀ", "b": "ʙ", "c": "ᴄ", "d": "ᴅ", "e": "ᴇ",
    "f": "ғ", "g": "ɢ", "h": "ʜ", "i": "ɪ", "j": "ᴊ",
    "k": "ᴋ", "l": "ʟ", "m": "ᴍ", "n": "ɴ", "o": "ᴏ",
    "p": "ᴘ", "q": "ǫ", "r": "ʀ", "s": "s", "t": "ᴛ",
    "u": "ᴜ", "v": "ᴠ", "w": "ᴡ", "x": "x", "y": "ʏ",
    "z": "ᴢ"
}

# Fancy styles
fancy1_map = {
    "a": "α", "b": "в", "c": "¢", "d": "∂", "e": "є",
    "f": "ƒ", "g": "g", "h": "н", "i": "ι", "j": "נ",
    "k": "к", "l": "ℓ", "m": "м", "n": "η", "o": "σ",
    "p": "ρ", "q": "q", "r": "я", "s": "ѕ", "t": "т",
    "u": "υ", "v": "ν", "w": "ω", "x": "χ", "y": "у",
    "z": "z"
}

fancy2_map = {
    "a": "🅐", "b": "🅑", "c": "🅒", "d": "🅓", "e": "🅔",
    "f": "🅕", "g": "🅖", "h": "🅗", "i": "🅘", "j": "🅙",
    "k": "🅚", "l": "🅛", "m": "🅜", "n": "🅝", "o": "🅞",
    "p": "🅟", "q": "🅠", "r": "🅡", "s": "🅢", "t": "🅣",
    "u": "🅤", "v": "🅥", "w": "🅦", "x": "🅧", "y": "🅨",
    "z": "🅩"
}

fancy3_map = {
    "a": "𝖆", "b": "𝖇", "c": "𝖈", "d": "𝖉", "e": "𝖊",
    "f": "𝖋", "g": "𝖌", "h": "𝖍", "i": "𝖎", "j": "𝖏",
    "k": "𝖐", "l": "𝖑", "m": "𝖒", "n": "𝖓", "o": "𝖔",
    "p": "𝖕", "q": "𝖖", "r": "𝖗", "s": "𝖘", "t": "𝖙",
    "u": "𝖚", "v": "𝖛", "w": "𝖜", "x": "𝖝", "y": "𝖞",
    "z": "𝖟"
}

# ------------------ MAIN STYLES ------------------

FONTS = {
    "bold": bold_map,
    "italic": italic_map,
    "mono": mono_map,
    "double": double_map,
    "smallcaps": small_caps_map,
    "fancy1": fancy1_map,
    "fancy2": fancy2_map,
    "fancy3": fancy3_map,
}


def get_all_fonts():
    return list(FONTS.keys())


def convert_text(text: str, style: str) -> str:
    font_map = FONTS.get(style)

    if not font_map:
        return text

    return apply_font(text, font_map)
