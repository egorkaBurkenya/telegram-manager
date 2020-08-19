import telebot
import config
import random
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)

 
@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Как добавить в меня файл ?")
    item2 = types.KeyboardButton("Режимы работы")
    item3 = types.KeyboardButton("Узнать id чата")
 
    markup.add(item1, item2, item3)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, твои личный менаджер кода!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Узнать id чата':
            
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("как использовать?", callback_data='what')
            item2 = types.InlineKeyboardButton("спасибо!", callback_data='thanks')
            markup.add(item1, item2)
            
            bot.send_message(message.chat.id, message.chat.id, reply_markup=markup)

        elif message.text == 'Как добавить в меня файл ?':
            bot.send_message(message.chat.id, 'Для того что бы использовать меня, имортируйте в свой файл: os, файл sender.py \n\nimport os\nimport sender as s\n\nДля того что бы разобраться как использовать комманды читайте README.md файл на GitHub\n\n https://github.com/egorkaBurkenya/telegram-manager')

        elif message.text == 'Режимы работы':
            bot.send_message(message.chat.id, 'пока что доступен один режим работы')
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
           
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'what':
                bot.send_message(call.message.chat.id, 'id нужен вам для использования функций в вашем коде, для передачи ошибки именно на ваш канал')
            elif call.data == 'thanks':
                bot.send_message(call.message.chat.id, 'цмок')
    except Exception as e:
        print(repr(e))
 
bot.polling(none_stop=True)