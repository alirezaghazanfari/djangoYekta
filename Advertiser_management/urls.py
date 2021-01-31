from django.urls import  path

from . import views

urlpatterns = [
    path('show/',views.ShowAdPage.as_view(),name = 'ads'),
    path('create/',views.MAkingAdPage.as_view(),name='creation'),
    path('create/getPost/',views.MAkingAdPage.as_view(),name = 'creation'),
    path('click/<int:ad_id>/',views.GuideAfterClick.as_view(),name = 'ads link page'),
]