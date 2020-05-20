import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

# logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR
logging.basicConfig(filename='mybot.log', level=logging.INFO, format='%(asctime)s %(message)s')

PROXY = {'proxy_url': settings.PROXY_URL,
         'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}


def greet_user(update, context):

    print('Вызван /старт')
#    print(update)
    update.message.reply_text('Привет!')


def talk_to_me(update, context):

    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():

    mybot = Updater(settings.API_KEY, use_context = True, request_kwargs = PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


main()