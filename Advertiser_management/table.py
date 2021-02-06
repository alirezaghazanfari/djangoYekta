from django.db import models

from Advertiser_management.models import Ad


class table_1(models.Model):
    ad = models.ForeignKey(Ad,on_delete='CASCADE')
    clicks = models.IntegerField()
    time = models.TimeField()
class table_2(models.Model):
    ad = models.ForeignKey(Ad,on_delete='CASCADE')
    views = models.IntegerField()
    time = models.TimeField()

class table_3(models.Model):
    ad = models.ForeignKey(Ad,on_delete='CASCADE')
    clicks = models.IntegerField()
    time = models.TimeField()


class table_4(models.Model):
    ad = models.ForeignKey(Ad, on_delete='CASCADE')
    views = models.IntegerField()
    time = models.TimeField()
