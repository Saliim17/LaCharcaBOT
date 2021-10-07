import telebot

bot = telebot.TeleBot("1917927505:AAEXSn_XKGB6X4MYyIwxFLNmNyzLcjNZGZE", parse_mode=None)


@bot.message_handler(commands=['sapo'])
def send_welcome(message):
    bot.reply_to(message, "Hey sapete, ¿para qué me llamas?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()