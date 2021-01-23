from django.urls import  path

from . import views

urlpatterns = [
    path('',views.show_ad,name = 'ads'),
    path('create/',views.make_ad,name='creation'),
    path('create/getPost/',views.make_ad,name = 'handleForm'),
]