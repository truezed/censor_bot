import os
import re

import telebot

bot = telebot.TeleBot(os.getenv("token"))

ban_words = ["крым", "крим", "днр", "лнр", "тайвань", "китай"]


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message)
    text = re.sub('[^A-Za-z0-9а-яА-я]+', '', message.text.lower())
    if any(word in text for word in ban_words):
        bot.delete_message(message_id=message.message_id, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text=f"{message.from_user.first_name}, вы написали гадость!")


@bot.message_handler(content_types=['voice', 'sticker'])
def non_text_message_handler(message):
    bot.send_message(chat_id=message.chat.id,
                     text=f"{message.from_user.first_name}, получить пизды за неиспользование букв!")


bot.infinity_polling()
