from celery import shared_task
from Yektanet.celery import app
from Advertiser_management.models import Ad, Click, View
from datetime import datetime


@shared_task()
def add(x, y):
    print('sa')
    return x + y





@app.task
def test_1(ads):
    for i in ads:
        clicks = Click.objects.filter(created_at__hour__lte=datetime.now().hour-1, ad = i , created_at__date__lte=datetime.now()).count()

@app.task
def test_2(ads):
    for i in ads:
        views= View.objects.filter(created_at__hour__lte=datetime.now().hour-1, ad = i , created_at__date__lte=datetime.now()).count()


@app.task
def test_3(ads):
    start_time = datetime.now().replace(hour=00)
    certain_time = 24
    final_time = start_time.replace(hour=certain_time)
    for i in ads:
        clicks = Click.objects.filter(created_at__range=(start_time,final_time), ad = i , created_at__date__lte=datetime.now()).count()


@app.task
def test_4(ads):
    start_time = datetime.now().replace(hour=00)
    certain_time = 24
    final_time = start_time.replace(hour=certain_time)
    for i in ads:
        views = View.objects.filter(created_at__range=(start_time,final_time), ad = i , created_at__date__lte=datetime.now()).count()

