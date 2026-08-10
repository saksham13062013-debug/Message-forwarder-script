import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION_STRING = os.environ["SESSION_STRING"]

SOURCE = "@DAILY_GIFT_CODEEE"
DESTINATION = "@CODE13167"

client = TelegramClient(
    StringSession(SESSION_STRING),
    API_ID,
    API_HASH
)

# Lines containing these terms will NOT be copied.
FILTER_TERMS = (
    "register",
    "invitationcode",
    "jodhpur91.com",
    "http://",
    "https://",
)

def filter_message(text):
    lines = text.splitlines()
    kept = []

    for line in lines:
        if any(term in line.lower() for term in FILTER_TERMS):
            continue
        kept.append(line)

    # Clean up extra blank lines left by removed lines.
    result = "\n".join(kept)
    while "\n\n\n" in result:
        result = result.replace("\n\n\n", "\n\n")

    return result.strip()


@client.on(events.NewMessage(chats=SOURCE))
async def copy_message(event):
    if not event.message.message:
        return

    filtered_text = filter_message(event.message.message)

    # Don't send anything if the whole message was filtered out.
    if not filtered_text:
        return

    try:
        await client.send_message(DESTINATION, filtered_text)
        print("Filtered message copied successfully.", flush=True)
    except Exception as e:
        print(f"Error: {e}", flush=True)


print("Auto-copy started with register/link filter...", flush=True)
client.start()
client.run_until_disconnected()
