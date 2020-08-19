import telebot
import config


bot = telebot.TeleBot(config.TOKEN)

def telegramSender(fileName = "main.py", message_type = "error", chat_id = config.ADMIN_CHAT_ID, message = "message"): 
    
    if message_type.lower() == 'error':
        bot.send_message(chat_id, f'{fileName} have some ERROR\n\n{message}')
    
    elif message_type.lower() == 'print':
        bot.send_message(chat_id, f'{fileName}\n\n{message}')
    
    elif message_type.lower().split(' ')[0] == 'message':
        message_header = message_type.lower().split(' ')[1]
        bot.send_message(chat_id, f'{message_header}\n\n{message}')


