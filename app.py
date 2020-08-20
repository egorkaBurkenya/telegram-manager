import telebot
import random
import json
from telebot import types
 
with open('config.json', 'r', encoding='utf-8') as fh: 
    data = json.load(fh)

bot = telebot.TeleBot(data['TOKEN'])

 
@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Как добавить меня в файл ?")
    item2 = types.KeyboardButton("Узнать id чата")
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, твои личный менаджер кода!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['commands'])
def commands(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Режимы работы")
    item2 = types.KeyboardButton("id чата")
 
    markup.add(item1, item2)
 
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

        elif message.text == 'id чата':
            bot.send_message(message.chat.id, message.chat.id)
        
        elif message.text == 'Как добавить меня в файл ?':
            bot.send_message(message.chat.id, 'Для того что бы использовать меня, имортируйте в свой файл: os, файл sender.py \n\nimport os\nimport sender as s\n\nДля того что бы разобраться как использовать комманды читайте README.md файл на GitHub\n\n https://github.com/egorkaBurkenya/telegram-manager')

        elif message.text == 'Режимы работы':
           
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("all")
            item2 = types.KeyboardButton("errors")
            item3 = types.KeyboardButton("message")
            item4 = types.KeyboardButton("print")
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'выберите режим работы!', reply_markup=markup)
        
        elif message.text == 'all':
            with open('config.json', 'r', encoding='utf-8') as fh: 
                data = json.load(fh)
            if data["OPERATING_MODE"] == '0':
                bot.send_message(message.chat.id, 'Уже включен данный режим') 
            else: 
                data["OPERATING_MODE"] = '0' 
                with open('config.json', 'w', encoding='utf-8') as fh:
                    fh.write(json.dumps(data, ensure_ascii=False))
                bot.send_message(message.chat.id, 'Готово! теперь все уведомления будут работать!')
        
        elif message.text == 'errors':
            with open('config.json', 'r', encoding='utf-8') as fh: 
                data = json.load(fh)
            if data["OPERATING_MODE"] == '1':
                bot.send_message(message.chat.id, 'Уже включен данный режим') 
            else: 
                data["OPERATING_MODE"] = '1' 
                with open('config.json', 'w', encoding='utf-8') as fh:
                    fh.write(json.dumps(data, ensure_ascii=False))
                bot.send_message(message.chat.id, 'Готово! теперь только ошибки потревожат вас')
        elif message.text == 'message':
            with open('config.json', 'r', encoding='utf-8') as fh: 
                data = json.load(fh)
            if data["OPERATING_MODE"] == '2':
                bot.send_message(message.chat.id, 'Уже включен данный режим') 
            else: 
                data["OPERATING_MODE"] = '2' 
                with open('config.json', 'w', encoding='utf-8') as fh:
                    fh.write(json.dumps(data, ensure_ascii=False))
                bot.send_message(message.chat.id, 'Готово! теперь только сообщения потревожат вас')
            
        elif message.text == 'print':
            with open('config.json', 'r', encoding='utf-8') as fh: 
                data = json.load(fh)
            if data["OPERATING_MODE"] == '3':
                bot.send_message(message.chat.id, 'Уже включен данный режим') 
            else: 
                data["OPERATING_MODE"] = '3' 
                with open('config.json', 'w', encoding='utf-8') as fh:
                    fh.write(json.dumps(data, ensure_ascii=False))
                bot.send_message(message.chat.id, 'Готово! теперь только print потревожит вас')
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