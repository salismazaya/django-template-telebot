from django.conf import settings
from django.urls import path
from main import views

urlpatterns = [
    path('supersecret/hooks/telegram/{}'.format(settings.TELEGRAM_BOT_TOKEN), views.telegram_webhook, name = 'telegram-webhook'),
    path('supersecret/hooks/telegram/set/', views.set_telegram_webhook, name = 'set-telegram-webhook')
]