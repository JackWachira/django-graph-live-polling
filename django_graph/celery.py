import os

from decouple import config
from django.conf import settings

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_graph.settings')

app = Celery('random_generator', broker=config(
    'REDISCLOUD_URL', default='redis://localhost:6379'))

app.conf.timezone = 'UTC'

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.broker_url = config(
    'REDISCLOUD_URL', default='redis://localhost:6379')
app.conf.result_backend = config(
    'REDISCLOUD_URL', default='redis://localhost:6379')
