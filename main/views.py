from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from telebot import types
from main.bot import bot
import traceback

def telegram_webhook(request: HttpRequest):
    try:
        update = types.Update.de_json(request.body.decode())
        bot.process_new_updates([update])
    except:
        traceback.print_exc()

    return HttpResponse('!')

def set_telegram_webhook(request: HttpRequest):
    bot.remove_webhook()
    bot.set_webhook('https://{}{}'.format(request.get_host(), reverse('telegram-webhook')))

    return HttpResponse('!')
