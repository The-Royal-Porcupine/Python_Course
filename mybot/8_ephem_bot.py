"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from datetime import datetime

import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

import settings

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)

PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def constellation(bot, update):
    planet = update.message.text.split()[1]

    if hasattr(ephem, planet):
        if hasattr(ephem, planet):
            planet = getattr(ephem, planet)()
            planet.compute()
            cons = ephem.constellation(planet)
            update.message.reply_text(cons)
    else:
        text = 'Такой планеты нет, дружок'
        update.message.reply_text(text)


def count_words(bot, update):
    sentence = update.message.text.split()[1:]
    if len(sentence) == 0:
        text = 'Тут нечего считать, дружок'
        update.message.reply_text(text)
    elif all(word.isdigit() for word in sentence):
        text = 'Слова из цифр ввёл, дружок?'
        update.message.reply_text(text)
    elif all(word.isalpha() for word in sentence):
        text = f'В предложении вот столько слов: {len(sentence)}'
        update.message.reply_text(text)
    else:
        text = f'Дружок, в какие-то слова проникли цифры или что похуже!'
        update.message.reply_text(text)


def full_moon(bot, update):
    today = datetime.today().date()
    moon_info = ephem.next_full_moon(today)
    text = f'Следующее полнолуние наступит {moon_info}'
    update.message.reply_text(text)

# Не доделала, пока не понятно
def cities_play(bot, update, context):
    cities = ['Москва', 'Воронеж', 'Астрахань', 'Владивосток', 'Караганда']
    user_city = сontext.a
    print(update.message.text)
    # if not update.message.text:
    #     update.message.reply_text('Введи город, дружок')
    # else:
    #     update.message.reply_text(user_city)



def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY)

    commands = [
        ["start", greet_user],
        ["planet", constellation],
        ["wordcount", count_words],
        ["next_full_moon", full_moon]
    ]

    dp = mybot.dispatcher
    # dp.add_handler(ConversationHandler(entry_points=[CommandHandler("cities", cities_play)],
    #                                    states={},
    #                                    fallbacks=[]
    #                                    ))
    for command, function in commands:
        dp.add_handler(CommandHandler(command, function))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
