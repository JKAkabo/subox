import django_heroku

from .base import *

DEBUG = True

# Activate Django-Heroku
django_heroku.settings(locals())

