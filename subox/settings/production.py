import django_heroku

from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

# Activate Django-Heroku
django_heroku.settings(locals())
