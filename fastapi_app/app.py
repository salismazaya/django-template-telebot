from dotenv import load_dotenv
import os, django

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

from fastapi import FastAPI, Request
from django.conf import settings
from telebot import types
from main.bot import bot

app = FastAPI()

@app.post('/supersecret/hooks/{}'.format(settings.TELEGRAM_BOT_TOKEN))
async def telegram_webhook(update: dict):
    if update:
        update = types.Update.de_json(update)
        await bot.process_new_updates([update])
    
    return '!'

@app.get('/supersecret/hooks/set')
async def set_telegram_webhook(request: Request):
    url = str(request.base_url).replace('http://', 'https://')
    url = str(url).removesuffix('/') + \
    '/telegram/supersecret/hooks/{}'.format(settings.TELEGRAM_BOT_TOKEN)
    await bot.remove_webhook()
    await bot.set_webhook(url)

    return '!'