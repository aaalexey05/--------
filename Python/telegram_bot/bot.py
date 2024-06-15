import telebot

bot = telebot.TeleBot('6865556440:AAGZnh7OkUP-w2gwNlG-PYTlFmslkzFwE5w')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Hello!")

@bot.message_handler(command=['help'])
def help(message):
    bot.send_message(message.chat.id, "Help information:\n-/start - запуск бота")
    
bot.polling(non_stop=True)