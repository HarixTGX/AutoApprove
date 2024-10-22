import config

app = Client("Bot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)



names = []  # List to store names
message_id = None  # Store the message ID to edit later

@app.on_message(filters.group & filters.text & ~filters.command(['done']))
async def handle_message(client, message):
    global names, message_id

    # Add the new name to the list
    names.append(message.text.strip())

    # Format the list of names
    compiled_message = "\n".join([f"{i + 1}. {name}" for i, name in enumerate(names)])

    # If it's the first message, send it; otherwise, edit the existing one
    if message_id is None:
        sent_message = await message.reply_text(compiled_message)
        message_id = sent_message.id  # Store the message ID for future edits
    else:
        await client.edit_message_text(
            chat_id=message.chat.id,
            message_id=message_id,
            text=compiled_message
        )

# Start command handler
@app.on_message(filters.command("done"))
async def start(client, message):
    global names, message_id
    names = []  # Clear the list when /start is called
    message_id = None  # Reset the message ID
    await message.reply_text("Single Page All Message Done ✅")
    
#run
print(f"Starting {app.name}")
try:
    app.run()
except:
    traceback.print_exc()
