import ptbot
import os

from pytimeparse import parse
from dotenv import load_dotenv

TG_TOKEN = os.getenv("TELEGRAM_TOKEN")
TG_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def reply(chat_id, text):
    message_id = bot.send_message(chat_id, "Запускаю таймер!")
    bot.create_countdown(parse(text), notify_progress, chat_id=chat_id, message_id=message_id, text=text)
    bot.create_timer(parse(text), answer, chat_id=chat_id)


def notify_progress(secs_left, chat_id, message_id, text):
    bot.update_message(chat_id, message_id, "Осталось {} секунд\n{}".format(secs_left, render_progressbar(parse(text), parse(text) - secs_left)))


def answer(chat_id):
    bot.send_message(chat_id, "Время вышло!")


if __name__ == '__main__':
    load_dotenv()
    TG_TOKEN = os.getenv("TELEGRAM_TOKEN")
    TG_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(reply)
    bot.run_bot()
