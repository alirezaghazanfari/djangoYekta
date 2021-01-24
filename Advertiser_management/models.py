from django.db import models

# Create your models here.
class Advertiser(models.Model):
    name = models.CharField(max_length=200 ,default="")
    advertiser_id = models.IntegerField(primary_key=True , default=0)
    clicks = 0
    views = 0
    ads=[]
    def __str__(self):
        return self.name
    totalClciks = 0
    def get_name(self):
        return self.name
    def set_name(self,newName):
        self.name = newName
    @staticmethod
    def help():
        message = "this is help message"
        return message

    def describe_me(self):
        description = "this class is advertiser"
        return description

    def inc_clicks(self):
        self.clicks +=1
        Advertiser.totalClciks+=1

    @staticmethod
    def get_total_clicks():
        return Advertiser.totalClciks




class Ad(models.Model):
    views = 0
    clicks = 0
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    image = models.URLField(max_length=200)
    advertiser = models.ForeignKey(Advertiser,on_delete=models.CASCADE)
    def __str__(self):
        return self.title




    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title

    def get_image(self):
        return self.image

    def set_image(self, new_img):
        self.image = new_img

    def get_link(self):
        return self.link

    def set_link(self, new_link):
        self.link = new_link

    def get_advertiser(self):
        return self.advertiser

    def set_advertiser(self, new_advertiser):
        self.advertiser = new_advertiser

    def inc_clicks(self):
        self.clicks+=1
        self.advertiser.inc_clicks()

    def inc_views(self):
        self.views+=1

    def describe_me(self):
        message = "this is class Ad"
        return message

