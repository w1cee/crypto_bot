# -*- coding: utf-8 -*-
# bot by w1cee

from bs4 import BeautifulSoup
import requests
import re
import telebot

TOKEN = 'TOKEN'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    buttons = telebot.types.ReplyKeyboardMarkup(True)
    buttons.row('Bitcoin', 'Ethereum', 'Dogecoin')
    bot.send_message(message.chat.id, 'Hello, send me the name of any cryptocurrency and I will send you the price!',
                     reply_markup=buttons)


@bot.message_handler(content_types=['text'])
def get_price(message):
    user_input = message.text
    name_of_crypto = user_input.replace(' ', '-')
    url = f'https://coinmarketcap.com/currencies/{name_of_crypto}/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        block = soup.find_all('div', class_='priceValue')  # bs4.element.ResultSet
        element = str(block)
        price = re.findall(r'[$][\d]*[,]?[\d]*[.]?[\d]*', element)
        price = price.pop(0)
        markdown = """
                   *bold text*
                   """
        bot.send_message(message.chat.id, f'*1 {name_of_crypto.upper()}* = '
                                          f'*{price}*', parse_mode='markdown')
    elif response.status_code == 404:
        bot.send_message(message.chat.id, 'Are you sure this cryptocurrency exists?')
    else:
        bot.send_message(message.chat.id, 'Something went wrong..')


bot.infinity_polling()
