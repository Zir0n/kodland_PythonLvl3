from config import *
from random import choice
print(token)

import telebot

API_TOKEN = token
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я Botrik.  
Я здесь, чтобы обрабатывать ваши команды и сообщения. Если хочешь узнать, какие команды Botrik умеет выполнять, то просто напиши /info.\
""")

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, """\
Команды, которые способен выполнить огурчик Rik: /start, /help, /info, /coin\
""")


@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()