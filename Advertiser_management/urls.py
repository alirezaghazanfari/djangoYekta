from django.urls import  path

from . import views

urlpatterns = [
    path('show/',views.ShowAdPage.as_view(),name = 'ads'),
    path('create/',views.make_ad,name='creation'),
    path('create/getPost/',views.make_ad,name = 'creation'),
    path('click/<int:ad_id>/',views.guide_user_after_click,name = 'ads'),
]