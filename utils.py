import telebot


def get_vote_text(name, yes, no):
    return "Объявить {name} врагом народа \n✅ Да, отправление смерть! {num1}/1 " \
           "\n❌ Отрицательно, пощада {num2}/10305382" \
        .format(name=name, num1=yes, num2=no)


def extract_arg(arg):
    return arg.split()[1:]


def register_handlers(bot: telebot.TeleBot):
    from handlers import get_rating, text_handler, non_text_message_handler, vote_public_enemy, get_anek

    bot.register_message_handler(commands=["anek"], callback=get_anek, pass_bot=True)
    bot.register_message_handler(commands=["rating"], callback=get_rating, pass_bot=True)
    bot.register_message_handler(commands=["votekick"], callback=vote_public_enemy, pass_bot=True)
    bot.register_message_handler(content_types=["voice"], callback=non_text_message_handler, pass_bot=True)
    bot.register_message_handler(content_types=["text"], callback=text_handler, pass_bot=True)
