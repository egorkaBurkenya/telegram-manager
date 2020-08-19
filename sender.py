import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

def telegramErrorSender(message_type, chat_id, message): 
    if message_type.lower() == 'error':
        bot.send_message(chat_id, f'ERROR \n {message}')
