from telegram.ext import Updater
from telegram.ext import CommandHandler


def sms(bot, update):
    print("something")
    bot.message.reply_text('Привет\nЯ первый бот Doc-а')


def main():
    first_bot = Updater("1646319872:AAFRKYYKLkCCeuG-3AWYYoGeNmT_Z566oYE", use_context=True)

    first_bot.dispatcher.add_handler(CommandHandler('start', sms))
    first_bot.start_polling()
    first_bot.idle()


main()
