import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION_STRING = os.environ["SESSION_STRING"]

SOURCE = "@Vanshupredictionsking"
DESTINATION = "@CODE13167"

client = TelegramClient(
    StringSession(SESSION_STRING),
    API_ID,
    API_HASH
)


@client.on(events.NewMessage(chats=SOURCE))
async def copy_message(event):
    if not event.message.message:
        return

    try:
        await client.send_message(
            DESTINATION,
            event.message.message
        )
        print("Message copied successfully.", flush=True)
    except Exception as e:
        print(f"Error: {e}", flush=True)


print("Auto-copy started...", flush=True)
client.start()
client.run_until_disconnected()
