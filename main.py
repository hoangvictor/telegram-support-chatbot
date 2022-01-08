from telegram.ext import *
import responses
import requests
import re

API_telegram = "5033657181:AAGxPaISiZbtHehBPZTtSe6NNDDm48y6iuY"
API_coinmarketcap = "843a3f27-9c53-4394-84c9-d781713d7651"

print("Bot started...")


def start_command(update, context):
    update.message.reply_text('Type something random to get started!')


def help_command(update, context):
    update.message.reply_text('You can find it on Google')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = responses.responses_cases(text)

    update.message.reply_text(response)


def error(update, context):
    print("Error occured")


def main():
    updater = Updater(API_telegram, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling()
    updater.idle()


main()

# This example uses Python 2.7 and the python-request library.
