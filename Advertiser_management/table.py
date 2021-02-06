from django.db import models


class table_1(models.Model):
    ad = models.CharField()
    clicks = models.IntegerField()
class table_2(models.Model):
    ad = models.CharField()
    views = models.IntegerField()
class table_3(models.Model):
    ad = models.CharField()
    clicks = models.IntegerField()

class table_4(models.Model):
        ad = models.CharField()
        views = models.IntegerField()