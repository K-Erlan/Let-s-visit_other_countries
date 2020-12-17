import telebot
from telebot import types
# Global bot setting
TOKEN = ''

# Code
PRODUCTS = {}

print('Working')
bot = telebot.TeleBot(TOKEN)

def add_category(name):
    PRODUCTS[name] = []


def add_product(to, name, price, photo):
    PRODUCTS[to].append([name, price, photo])
