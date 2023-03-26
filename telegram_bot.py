import telegram
from dotenv import load_dotenv
import os
load_dotenv()

ACCESS_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
bot = telegram.Bot(token=ACCESS_TOKEN)

async def bot_error_message(message):
    await bot.send_message(CHAT_ID, text=message)

async def bot_debug(message):
    pass
    # await bot.send_message(CHAT_ID, text=message)

async def bot_message(message):
    await bot.send_message(CHAT_ID, text=message)
