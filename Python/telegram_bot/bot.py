import telebot

bot = telebot.TeleBot('6865556440:AAGZnh7OkUP-w2gwNlG-PYTlFmslkzFwE5w')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, message)


@bot.message_handler(command=['help'])
def main(message):
    bot.send_message(message.chat.id, "<b>Help</b> <em><u>information</u></em>", parse_mode="html")


bot.polling(non_stop=True)
