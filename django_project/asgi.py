"""
ASGI config for django_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

from dotenv import load_dotenv
from starlette.applications import Starlette
import os

load_dotenv()

from django.core.asgi import get_asgi_application
from fastapi_app.app import app as fastapi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

django_application = get_asgi_application()

application = Starlette()
application.mount('/telegram', fastapi_application)
application.mount('/', django_application) 