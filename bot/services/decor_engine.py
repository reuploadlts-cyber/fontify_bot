# Emoji + Symbol decoration engine

DECOR_STYLES = {
    "sparkle": ("✨", "✨"),
    "fire": ("🔥", "🔥"),
    "hearts": ("💖", "💖"),
    "stars": ("🌟", "🌟"),
    "crown": ("👑", "👑"),
    "lightning": ("⚡", "⚡"),
    "flowers": ("🌸", "🌸"),
}

WRAPPERS = {
    "box": ("『", "』"),
    "fancy": ("꧁", "꧂"),
    "stars": ("★", "★"),
    "dots": ("•", "•"),
    "hearts": ("♥", "♥"),
}


def apply_decor(text: str, style: str) -> str:
    emojis = DECOR_STYLES.get(style)

    if not emojis:
        return text

    left, right = emojis
    return f"{left} {text} {right}"


def apply_wrapper(text: str, style: str) -> str:
    wrapper = WRAPPERS.get(style)

    if not wrapper:
        return text

    left, right = wrapper
    return f"{left} {text} {right}"
