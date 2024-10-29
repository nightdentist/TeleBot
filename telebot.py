import ptbot
import os

from dotenv import load_dotenv

load_dotenv()

TG_TOKEN = os.getenv("TELEGRAM_TOKEN")
TG_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
bot = ptbot.Bot(TG_TOKEN)
bot.send_message(TG_CHAT_ID, "Бот запущен")
