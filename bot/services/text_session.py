# Simple in-memory session (per user)

user_text_session = {}


def set_user_text(user_id: int, text: str):
    user_text_session[user_id] = text


def get_user_text(user_id: int):
    return user_text_session.get(user_id)


def clear_user_text(user_id: int):
    user_text_session.pop(user_id, None)
