import os
import random
import re

import telebot
import constants as const

bot = telebot.TeleBot(os.getenv("token"))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message)
    input_message = message.text.lower()
    text = re.sub('[^A-Za-z0-9а-яА-я]+', '', input_message)
    if any(word in text for word in const.BAN_WORDS):
        bot.delete_message(message_id=message.message_id, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text=f"{message.from_user.first_name}, вы написали гадость!")
    if re.search(const.CHINA_REGEX, input_message):
        bot.send_photo(message.chat.id, random.choice(const.PLUS_CREDITS_IMAGES))
    if re.search(const.TAIWAN_REGEX, input_message):
        bot.send_photo(message.chat.id, random.choice(const.MINUS_CREDITS_IMAGES))


@bot.message_handler(content_types=['voice', 'sticker'])
def non_text_message_handler(message):
    bot.send_message(chat_id=message.chat.id,
                     text=f"{message.from_user.first_name}, получить пизды за неиспользование букв!")


bot.infinity_polling()
