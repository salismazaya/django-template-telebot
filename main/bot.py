from email import message
from django.conf import settings
from telebot import TeleBot

bot = TeleBot(settings.TELEGRAM_BOT_TOKEN, threaded = False)