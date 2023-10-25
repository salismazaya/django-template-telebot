from django.apps import AppConfig
from django.conf import settings
import os, threading

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        super().ready()

        run_once = os.environ.get('DJANGO_MAIN_RUN_ONCE') == 'True'
        if run_once:
            return

        os.environ['DJANGO_MAIN_RUN_ONCE'] = 'True'

        import main.bot

        if settings.DEBUG:
            t = threading.Thread(target = main.bot.bot.polling)
            t.setDaemon(True)
            t.start()