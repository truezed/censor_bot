import re

import telebot

bot = telebot.TeleBot("5585456773:AAHTqq_grxE9hJF7nKX3FU5RoxJuoFPUpyQ")

ban_words = ["крым", "крим", "днр", "лнр", "тайвань", "китай"]


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message)
    text = re.sub('[^A-Za-z0-9а-яА-я]+', '', message.text.lower())
    print(text)
    if any(word in text for word in ban_words):
        bot.delete_message(message_id=message.message_id, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text=f"{message.from_user.first_name}, вы пишете гадости  .ю!")


bot.infinity_polling()
