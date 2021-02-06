from django.urls import  path

from . import views

urlpatterns = [
    path('show/',views.ShowAdPageAPI.as_view(),name = 'ads'),
    path('create/',views.MAkingAdPage.as_view(),name='creation'),
    path('create/getPost/',views.MAkingAdPage.as_view(),name = 'creation'),
    path('click/<int:ad_id>/',views.GuideAfterClickAPI.as_view(),name = 'ads link page'),
    path('detail/',views.ShowDetails.as_view(),name = 'details'),
]