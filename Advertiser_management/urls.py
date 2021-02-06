from django.urls import  path

from . import views

urlpatterns = [
    path('show/',views.ShowAdPageAPI.as_view(),name = 'ads'),
    path('create/',views.MakeAdPageAPI.as_view(),name='creation'),
    path('create/getPost/',views.MakeAdPageAPI.as_view(),name = 'creation'),
    path('click/<int:ad_id>/',views.GuideAfterClick.as_view(),name = 'ads link page'),
    path('detail/hour/',views.ShowDetailAPIIOfFilterHour.as_view(),name = 'details'),
    path('detail/rate/',views.ShowDetailAPIOfRate.as_view(),name='rate'),
    path('detail/ip/',views.ShowDetailAPIOfIP.as_view(),name = 'ip'),
]