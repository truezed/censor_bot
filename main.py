import os
import random
import re
import time

import telebot
import telebot.types as types
import constants as const

bot = telebot.TeleBot(os.getenv("token"))


def extract_arg(arg):
    return arg.split()[1:]


@bot.message_handler(commands=["startvote"])
def vote_public_enemy(message):
    args = extract_arg(message.text)
    if not args:
        bot.send_message(message.chat.id, "Укажите имя или тег гражданина")
    general_name = args[0]
    if general_name == "":
        bot.send_message(message.chat.id, "Укажите имя или тег гражданина")
    bot.send_message(message.chat.id, get_vote_text(general_name, 0, 0))


def get_vote_text(name, yes, no):
    return "Объявить {name} врагом народа \n✅ Да, отправление смерть! {num1}/1 " \
           "\n❌ Отрицательно, пощада {num2}/10305382"\
        .format(name=name, num1=yes, num2=no)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message)
    input_message = message.text.lower()
    text = re.sub('[^A-Za-z0-9а-яА-я]+', '', input_message)
    if any(word in text for word in const.BAN_WORDS):
        bot.delete_message(message_id=message.message_id, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text=f"{message.from_user.first_name}, вы написали гадость!")

    if re.search(const.CHINA_REGEX, input_message):
        bot.send_photo(message.chat.id,
                       random.choice(const.PLUS_CREDITS_IMAGES),
                       reply_to_message_id=message.message_id)
    if re.search(const.TAIWAN_REGEX, input_message):
        bot.send_photo(message.chat.id,
                       random.choice(const.MINUS_CREDITS_IMAGES),
                       reply_to_message_id=message.message_id)


@bot.message_handler(content_types=['voice', 'sticker'])
def non_text_message_handler(message):
    bot.reply_to(message, text=f"{message.from_user.first_name}, получить пизды за неиспользование букв!")


bot.infinity_polling()
