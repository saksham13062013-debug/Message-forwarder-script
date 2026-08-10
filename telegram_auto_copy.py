from telethon import TelegramClient, events

API_ID = 31509376
API_HASH = "REPLACE_WITH_YOUR_API_HASH"

SOURCE = "@DAILY_GIFT_CODEEE"
DESTINATION = "@CODE13167"

client = TelegramClient("auto_forward_session", API_ID, API_HASH)


@client.on(events.NewMessage(chats=SOURCE))
async def copy_message(event):
    # Text messages only
    if not event.message.message:
        return

    try:
        await client.send_message(
            DESTINATION,
            event.message.message
        )
        print("Message copied successfully.")

    except Exception as e:
        print("Error:", e)


print("Auto-copy started...")
client.start()
client.run_until_disconnected()
