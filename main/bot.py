from django.conf import settings
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(settings.TELEGRAM_BOT_TOKEN)