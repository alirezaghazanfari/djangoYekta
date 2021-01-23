from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Ad
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import View
from .forms import data_form

from .models import Ad,Advertiser


# Create your views here.
def show_ad(request):
    if request.method == 'POST':
       pass
    else:
        pass
        #list_advertisers = Advertiser.objects.order_by(pk = )
        #return render(request, 'Advertiser_management/ads.html', {
         #    'Ads': listOfAds,
          #  })

def guide_user_after_click(request,ad_id):
   ad = get_object_or_404(Ad,pk = ad_id)
   ad.incClicks()
   ad.incViews()
   ad.save()
   return HttpResponseRedirect(ad.get_link())

def make_ad(request):
    if request.method == 'POST':
        form = data_form(request.POST)
        if form.is_valid():
            advertiser_find = form.cleaned_data.get('advertiser')
            advertiser = Advertiser.objects.get(Advertiser_id=advertiser_find)
            ad = Ad(title=form.cleaned_data.get('title') , link=form.cleaned_data.get('link') , img_url= form.cleaned_data.get('img_url') , advertiser= advertiser)
            ad.save()
            return HttpResponseRedirect('/ads/show/')
    else:
        form = data_form()
    return render(request, 'Advertiser_management/makingAd.html', {'form':form})


def handleCreationAd(request):
    title = request.POST['title']
    print(title)


