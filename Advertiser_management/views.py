from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Ad
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import View
from .forms import data_form

from .models import Ad


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
    if request.method == 'POST':
        form = data_form(request.POST)
        if form.is_valid():
            ad = Ad(title=form.title , link=form.link , img_url= form.img_url , advertiser_id= form.advertiser_id)
            ad.save()
            return HttpResponseRedirect(reverse('ads'))
    else:
        form = data_form()
    return render(request, 'Advertiser_management/makingAd.html', {'form':form})


def handleCreationAd(request):
    title = request.POST['title']
    print(title)


