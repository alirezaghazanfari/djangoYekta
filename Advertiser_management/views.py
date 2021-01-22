from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Ad,Advertiser
from django.shortcuts import render

# Create your views here.
def show_ad(request):
    return render(request,'../templates/Advertiser_management/ads.html',{})

def guide_user_after_clcick(request):
    pass

def make_ad(request):
    pass