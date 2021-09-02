import telebot
from telebot import TeleBot
from telebot import types
from datetime import datetime
from pycbrf import ExchangeRates

bot = telebot.TeleBot('1972971668:AAHSJFyM3AG-E_X_8uc5jKLoBjvNmFlx78c')
chat_id = '-1001539637265'


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.KeyboardButton('USD')
    itembtn2 = telebot.types.KeyboardButton('EUR')
    itembtn3 = telebot.types.KeyboardButton('JPY')
    itembtn4 = telebot.types.KeyboardButton('CHF')
    itembtn5 = telebot.types.KeyboardButton('GBP')
    itembtn6 = telebot.types.KeyboardButton('UAH')
    itembtn7 = telebot.types.KeyboardButton('KZT')
    itembtn8 = telebot.types.KeyboardButton('BYN')
    itembtn9 = telebot.types.KeyboardButton('TRY')
    itembtn10 = telebot.types.KeyboardButton('CNY')
    itembtn11 = telebot.types.KeyboardButton('AUD')
    itembtn12 = telebot.types.KeyboardButton('CAD')
    itembtn13 = telebot.types.KeyboardButton('PLN')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9,itembtn10,itembtn11,itembtn12,itembtn13)
    bot.send_message(chat_id=message.chat.id, text='<b>Hello! Choose the currency to see Exhange Rates!</b>', reply_markup=markup, parse_mode="html")


@bot.message_handler(content_types=['text'])
def message(message):
    message_norm = message.text.strip().lower()
    rates = ExchangeRates(datetime.now())
    bot.send_message(chat_id=message.chat.id, text=f"<b>{message_norm.upper()} rate is {float(rates[message_norm.upper()].rate)}</b>", parse_mode="html")


bot.polling(none_stop=True)