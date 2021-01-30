from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from ipware import get_client_ip
from .forms import data_form
from .models import Ad, Advertiser
from django.views.generic.base import TemplateView



# Create your views here.
class ShowAdPage(TemplateView):
    template_name = 'Advertiser_management/ads.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list_advertisers = list(Advertiser.objects.all())
        if len(list_advertisers) == 0:
            raise Http404('list of advertisers is empty')
        for advertiser1 in list_advertisers:
            advertiser1.ads = list(Ad.objects.filter(advertiser=advertiser1))
        context['advertisers'] = list_advertisers
        return context


def guide_user_after_click(request,ad_id):
        ad = get_object_or_404(Ad,pk = ad_id)
        user_id_str = request.META.get('HTTP_X_FORWARDED_FOR')
        ip = ''
        if user_id_str:
            ip = user_id_str.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        ad.inc_clicks(time=timezone.now(),user=ip)
        ad.inc_views(time=timezone.now(),user=ip)
        ad.save()
        return HttpResponseRedirect(ad.get_link())




def make_ad(request):
    if request.method == 'POST':
        form = data_form(request.POST)
        if form.is_valid():
          try:
            advertiser_find = form.cleaned_data.get('advertiser')
            advertiser = Advertiser.objects.get(advertiser_id=advertiser_find)
            ad = Ad(title=form.cleaned_data.get('title') , link=form.cleaned_data.get('link') , image= form.cleaned_data.get('image') , advertiser= advertiser)
            ad.save()
            return HttpResponseRedirect('/ads/show/')
          except:
              raise Http404('the error is in finding advertiser')

    else:
        form = data_form()
    return render(request, 'Advertiser_management/makingAd.html', {'form':form})



