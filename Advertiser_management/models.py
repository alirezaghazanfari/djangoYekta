from django.db import models

# Create your models here.
class Advertiser(models.Model):
    name = models.CharField(max_length=200 ,default="")
    advertiser_id = models.IntegerField(primary_key=True , default=0)

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

    @staticmethod
    def get_total_clicks():
        return Advertiser.totalClciks




class Ad(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    image = models.URLField(max_length=200)
    advertiser = models.ForeignKey(Advertiser,on_delete=models.CASCADE)
    approve = models.BooleanField(default=False )
    def __str__(self):
        return self.title
    def get_title(self):
        return self.title
    def approve_ad(self):
        self.approve = True
        self.save()
    def get_approve(self):
        return self.approve
    def set_approve(self,new_approve):
        self.approve = new_approve

        
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

    def inc_clicks(self,time,user):
        click = Click(ad= self , time= time , user_id= user)
        click.save()

    def inc_views(self,time,user):
        view = View(ad=self , time= time , user_id=user)
        view.save()

    def describe_me(self):
        message = "this is class Ad"
        return message


class Click(models.Model):
    ad = models.ForeignKey(Ad,on_delete=models.CASCADE,default=None)
    time = models.TimeField()
    user_id = models.CharField(max_length=200)

class View(models.Model):
    ad = models.ForeignKey(Ad,on_delete=models.CASCADE,default=None)
    time = models.TimeField()
    user_id = models.CharField(max_length=200)


