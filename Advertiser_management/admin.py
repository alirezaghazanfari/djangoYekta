from django.contrib import admin
from .models import Advertiser,Ad
# Register your models here.
admin.site.register(Advertiser)
class AdAdmin(admin.ModelAdmin):
     fields = ('approve',('title','link','image','advertiser',))
     readonly_fields =  ('title','link','image','advertiser',)
     list_display = ('title','advertiser','approve')
     list_filter = ('approve',)
     search_fields = ['title__exact',]

admin.site.register(Ad,AdAdmin)


