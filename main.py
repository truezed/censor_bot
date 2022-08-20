import os
import telebot

from utils import register_handlers

bot = telebot.TeleBot(os.getenv("token"))

register_handlers(bot)
bot.infinity_polling()
