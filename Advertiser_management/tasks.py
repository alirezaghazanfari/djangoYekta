from celery import shared_task, Celery
from celery.schedules import crontab
# from Yektanet.celery import app
from Advertiser_management.models import Ad, Click, View
from datetime import datetime
from Yektanet.celery import app



@app.task
def test_1(ads):
    for i in ads:
        clicks = Click.objects.filter(created_at__hour__lte=datetime.now().hour - 1, ad=i,
                                      created_at__date__lte=datetime.now()).count()


@app.task
def test_2(ads):
    for i in ads:
        views = View.objects.filter(created_at__hour__lte=datetime.now().hour - 1, ad=i,
                                    created_at__date__lte=datetime.now()).count()


@app.task
def test_3(ads):
    start_time = datetime.now().replace(hour=00)
    certain_time = 24
    final_time = start_time.replace(hour=certain_time)
    for i in ads:
        clicks = Click.objects.filter(created_at__range=(start_time, final_time), ad=i,
                                      created_at__date__lte=datetime.now()).count()


@app.task
def test_4(ads):
    start_time = datetime.now().replace(hour=00)
    certain_time = 24
    final_time = start_time.replace(hour=certain_time)
    for i in ads:
        views = View.objects.filter(created_at__range=(start_time, final_time), ad=i,
                                    created_at__date__lte=datetime.now()).count()


@app.on_after_configure.connect
def setup_1(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=1), test_1.s(Ad.objects.all()), name='hour1')


@app.on_after_configure.connect
def setup_2(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=1), test_2.s(Ad.objects.all()), name='hour2')


@app.on_after_configure.connect
def setup_3(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=24), test_3.s(Ad.objects.all()), name='day1')


@app.on_after_configure.connect
def setup_4(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=24), test_4.s(Ad.objects.all()), name='day2')
