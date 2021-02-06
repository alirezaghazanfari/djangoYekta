from django.db import models


class table_1(models.Model):
    ad = models.CharField(max_length=200)
    clicks = models.IntegerField()
    time = models.TimeField()
class table_2(models.Model):
    ad = models.CharField(max_length=200)
    views = models.IntegerField()
    time = models.TimeField()

class table_3(models.Model):
    ad = models.CharField(max_length=200)
    clicks = models.IntegerField()
    time = models.TimeField()


class table_4(models.Model):
        ad = models.CharField(max_length=200)
        views = models.IntegerField()
        time = models.TimeField()
