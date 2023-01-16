import os
import requests
from pyrogram import *

from config import Config
from pyrogram.types import *

OWNER_USERNAME = Config.OWNER_USERNAME
BOT_TOKEN = Config.BOT_TOKEN
bot_id = Config.BOT_ID

bot = Client("MerissaChatbot", bot_token=BOT_TOKEN, api_id=6,
             api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e")

@bot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await message.reply(f"**Hey There, I'm** {BOT_NAME}. **An advanced chatbot with AI. \n\nAdd me to your group and chat with me!**",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Dev", url=f"https://t.me/{OWNER_USERNAME}"),
                                        InlineKeyboardButton(
                                            "Repo", url="https://github.com/MaybePrince/Merissa-Chatbot/tree/Sax-ChatBot")
                                    ]]
                            ),               
           )
   else:
       await message.reply("**I'm alive, check my pm to know more about me!**")

async def type_and_send(message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    query = message.text.strip()
    await message._client.send_chat_action(chat_id, "typing")
    response = requests.get(f"https://api.princexd.tech/chatbot?text={query}").json()["message"]
    await message.reply_text(response)
    await message._client.send_chat_action(chat_id, "cancel")


@bot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_text(
        "[GitHub](https://github.com/MaybePrince/Merissa-Chatbot/tree/Sax-ChatBot)"
        + " | [Group](t.me/MerissaxSupport)",
        disable_web_page_preview=True,
    )


@bot.on_message(filters.command("help"))
async def start(_, message):
    await luna.send_chat_action(message.chat.id, "typing")
    await sleep(2)
    await message.reply_text("/repo - Get Repo Link")


@bot.on_message(
    ~filters.private
    & filters.text
    & ~filters.command("help")
    group=69,
)
async def chat(_, message):
    if message.reply_to_message:
        if not message.reply_to_message.from_user:
            return
        from_user_id = message.reply_to_message.from_user.id
        if from_user_id != bot_id:
            return
    else:
        match = re.search(
            "[.|\n]{0,}luna[.|\n]{0,}",
            message.text.strip(),
            flags=re.IGNORECASE,
        )
        if not match:
            return
    await type_and_send(message)


@bot.on_message(
    filters.private & ~filters.command("help")
)
async def chatpm(_, message):
    if not message.text:
        return
    await type_and_send(message) 

print("Merissa Sex-Chatbot Started!")
bot.run()
