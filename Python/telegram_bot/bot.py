import telebot

bot = telebot.TeleBot('6865556440:AAGZnh7OkUP-w2gwNlG-PYTlFmslkzFwE5w')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Hello!")