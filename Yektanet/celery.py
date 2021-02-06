from __future__ import absolute_import,unicode_literals
from celery import Celery
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_example.settings')


app = Celery('tasks', backend='rpc://', broker='pyamqp://')
app.config_from_object('django.conf:settings',namespace='Celery')

app.autodiscover_tasks()