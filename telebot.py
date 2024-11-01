import ptbot
import os

from pytimeparse import parse

from dotenv import load_dotenv

load_dotenv()

TG_TOKEN = os.getenv("TELEGRAM_TOKEN")
TG_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def reply(chat_id, text):
    bot.create_countdown(parse(text), notify_progress, chat_id=chat_id)
    bot.create_timer(parse(text), answer, chat_id=chat_id)


def notify_progress(secs_left, chat_id):
    bot.send_message(chat_id, "Осталось секунд: {}".format(secs_left))


def answer(chat_id):
    bot.send_message(chat_id, "Время вышло!")


bot = ptbot.Bot(TG_TOKEN)
bot.reply_on_message(reply)
bot.run_bot()
