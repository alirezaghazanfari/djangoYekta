from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Ad,Advertiser
from django.shortcuts import render
from django.forms import Form
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import  loader
# Create your views here.
def show_ad(request):
    listOfAds = Ad.objects.order_by('advertiser_id')
    return render(request, 'Advertiser_management/ads.html', {
        'Ads': listOfAds,
    })

def guide_user_after_click(request,ad_id):
   ad = get_object_or_404(Ad,pk = ad_id)
   ad.incClicks()
   ad.incViews()
   ad.save()
   return HttpResponseRedirect(ad.get_link())

def make_ad(request):
    return render(request, 'Advertiser_management/makingAd.html', {})


def handleCreationAd(request):
    title = request.POST['title']
    print(title)