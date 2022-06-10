import telebot

bot = telebot.TeleBot('5519925137:AAHdYuBnKXZqQv8usp3tyhSi-u58bE4B0v4')

@bot.message_handler(content_types=['text'])
def repeat(message):
    bot.send_message(message.chat.id, message.text)
    
bot.polling(none_stop=True)