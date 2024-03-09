from pyrogram import Client, filters, errors
import os
from api_info import *

if not os.path.exists("pyrogram_session"):
    os.makedirs("pyrogram_session")

CHAT_ID = int(input("Chat id: "))
REACTION = input("Valid reaction (eg 🗿): ")
limit = int(input("Number of messages (including your own): "))

with Client(
    "my_session",
    workdir="pyrogram_session/",
    api_hash=api_hash,
    api_id=api_id,
) as app:

    messages = app.get_chat_history(CHAT_ID, limit=limit)
    for m in messages:
        if m.from_user.is_self:
            continue
        try:
            app.send_reaction(CHAT_ID, m.id, REACTION)
        except (
            errors.exceptions.bad_request_400.MessageIdInvalid,
            errors.exceptions.bad_request_400.MessageNotModified,
        ):
            pass  # message does not exist or reaction is already sent and matches
