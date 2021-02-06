from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

from Advertiser_management.models import Ad
from Advertiser_management.tasks import test_2, test_3, test_4, test_1

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Yektanet.settings')


app = Celery('tasks', backend='rpc://', broker='pyamqp://')
app.config_from_object('django.conf:settings',namespace='Celery')

app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_1(sender,**kwargs):
    sender.add_periodic_task(crontab(hour=1),test_1.s(Ad.objects.all()),name='hour1')
@app.on_after_configure.connect
def setup_2(sender,**kwargs):
    sender.add_periodic_task(crontab(hour=1),test_2.s(Ad.objects.all()),name='hour2')
@app.on_after_configure.connect
def setup_3(sender,**kwargs):
    sender.add_periodic_task(crontab(hour=24),test_3.s(Ad.objects.all()),name='day1')
@app.on_after_configure.connect
def setup_4(sender,**kwargs):
    sender.add_periodic_task(crontab(hour=24),test_4.s(Ad.objects.all()),name='day2')
