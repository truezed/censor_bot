import json
import random
import re

import requests
import telebot.types

import constants

from utils import get_vote_text, extract_arg


def text_handler(message: telebot.types.Message, bot: telebot.TeleBot):
    print(message)
    input_message = message.text.lower()
    text = re.sub('[^A-Za-z0-9а-яА-я]+', '', input_message)
    if any(word in text for word in constants.BAN_WORDS):
        bot.delete_message(message_id=message.message_id, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text=f"{message.from_user.first_name}, вы написали гадость!")

    if re.search(constants.CHINA_REGEX, input_message):
        bot.send_photo(message.chat.id,
                       random.choice(constants.PLUS_CREDITS_IMAGES),
                       reply_to_message_id=message.message_id)
    if re.search(constants.TAIWAN_REGEX, input_message):
        bot.send_photo(message.chat.id,
                       random.choice(constants.MINUS_CREDITS_IMAGES),
                       reply_to_message_id=message.message_id)


def non_text_message_handler(message: telebot.types.Message, bot: telebot.TeleBot):
    bot.reply_to(message, text=f"{message.from_user.first_name}, получает пизды за неиспользование букв!")


def vote_public_enemy(message: telebot.types.Message, bot: telebot.TeleBot):
    args = extract_arg(message.text)
    if not args:
        bot.send_message(message.chat.id, "Укажите имя или тег гражданина")
        return
    general_name = args[0]
    if general_name == "":
        bot.send_message(message.chat.id, "Укажите имя или тег гражданина")
        return
    bot.send_message(message.chat.id, get_vote_text(general_name, 0, 0))


def get_anek(message: telebot.types.Message, bot: telebot.TeleBot):
    if random.random() < 0.05:
        bot.send_message(message.chat.id, constants.ZWANZIG_ANEK)
        return

    anek = json.loads(requests.get(
        url=constants.ANEKDOT_API
    ).text.replace("\r\n", "\\r\\n").replace("\t", "\\t").replace("\n", "\\n")).get("content", "Нет анека :(")

    bot.send_message(message.chat.id, "#anek \n\n" + anek)


def get_rating(message: telebot.types.Message, bot: telebot.TeleBot):
    user_id = message.from_user.id
    rating = 0
    bot.reply_to(message, f"Ваш рейтинг: {rating}")
