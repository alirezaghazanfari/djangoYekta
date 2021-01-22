from django.db import models

# Create your models here.
class BaseAdvertiser(models.Model):
    def __init__(self,views=0,clicks=0):
        self.views = views
        self.clicks = clicks
    def describeMe(self):
        description = "this class is father of Ad and Advertiser classes. I am BaseAdvertising Class"
        return description

    def getClicks(self):
        return self.clicks

    def getViews(self):
        return self.views

    def incClicks(self):
        self.clicks = self.clicks + 1

    def incViews(self):
        self.views = self.views + 1





class Ad(BaseAdvertiser,models.Model):
    def __init__(self, id, title, img_url, link, advertiser,views = 0,clicks = 0):
        super().__init__(views,clicks)
        self.id = id
        self.title = title
        self.img_url = img_url
        self.link = link
        self.advertiser = advertiser


    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title

    def get_img_url(self):
        return self.img_url

    def set_img_url(self, new_url):
        self.img_url = new_url

    def get_link(self):
        return self.link

    def set_link(self, new_link):
        self.link = new_link

    def get_advertiser(self):
        return self.advertiser

    def set_advertiser(self, new_advertiser):
        self.advertiser = new_advertiser

    def incClicks(self):
        super().incClicks()
        self.advertiser.incClicks()

    def incViews(self):
        super().incViews()
        self.advertiser.incViews()

    def describeMe(self):
        message = "this is class Ad"
        return message



class Advertiser(BaseAdvertiser,models.Model):
    def __init__(self,id,name,views = 0 , clicks = 0):
        super().__init__(views,clicks)
        self.id = id
        self.name = name
    totalClciks = 0
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName
    @staticmethod
    def help():
        message = "this is help message"
        return message

    def describeMe(self):
        description = "this class is advertiser"
        return description

    def incClicks(self):
        super().incClicks()
        Advertiser.totalClciks+=1

    @staticmethod
    def getTotalClicks():
        return Advertiser.totalClciks





