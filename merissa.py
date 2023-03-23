import os
import requests
from pyrogram import *

from config import Config
from pyrogram.types import *

OWNER_USERNAME = Config.OWNER_USERNAME
BOT_TOKEN = Config.BOT_TOKEN
BOT_ID = int(BOT_TOKEN.split(":")[0])
BOT_NAME = Config.BOT_NAME

chatbot_group = 2

bot = Client("MerissaChatbot", bot_token=BOT_TOKEN, api_id=6,
             api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e")

@bot.on_message(filters.command("start") & ~filters.edited)
async def start(client, message):
   if message.chat.type == 'private':
       await message.reply(f"**Hey There, I'm** {BOT_NAME}. **An advanced chatbot with AI. \n\nAdd me to your group and chat with me!**",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Dev", url=f"https://t.me/{OWNER_USERNAME}"),
                                        InlineKeyboardButton(
                                            "Repo", url="https://github.com/Prince-Botz/Merissa-Chatbot")
                                    ]]
                            ),               
           )
   else:
       await message.reply("**I'm alive, check my pm to know more about me!**")

@bot.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.edited,
    group=chatbot_group,  
)
async def chatbot_talk(_, message: Message):
    chat = message.chat.id
    if not message.reply_to_message:
        return
    if not message.reply_to_message.from_user:
        return
    if message.reply_to_message.from_user.id != BOT_ID:
        return
    if message.text[0] == "/":
        return
    if chat:
        await bot.send_chat_action(message.chat.id, "typing")
        lang = tr.translate(message.text).src
        trtoen = (
            message.text if lang == "en" else tr.translate(message.text, dest="en").text
        ).replace(" ", "%20")
        text = trtoen.replace(" ", "%20") if len(message.text) < 2 else trtoen
        merissaurl = requests.get(
            f"https://api.princexd.tech/chatbot?text={text}"
        )
        textmsg = merissaurl.json()["message"]       
        await message.reply_text(msg.text)

print("Merissa Chatbot Started!")
bot.run()
