from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.db.models import QuerySet,Count
from .forms import data_form
from .models import Ad, Advertiser,Click,View
from datetime import time as time_making



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
        list_of_ads = Ad.objects.all()
        user_id_str = self.request.META.get('HTTP_X_FORWARDED_FOR')
        ip = ''
        if user_id_str:
            ip = user_id_str.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        for i in list_of_ads:
            i.inc_views(time=timezone.now(), user=ip)
            i.save()

        return context

class GuideAfterClick(RedirectView):
    permanent = False
    pattern_name = 'ads link page'
    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['ad_id'])
        user_id_str = self.request.META.get('HTTP_X_FORWARDED_FOR')
        ip = ''
        if user_id_str:
            ip = user_id_str.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        ad.inc_clicks(time=timezone.now(), user=ip)
        ad.save()
        return ad.get_link()


class MAkingAdPage(FormView):
    template_name = 'Advertiser_management/makingAd.html'
    form_class = data_form
    success_url = 'getPost/'
    def form_valid(self, form):
        try:
            advertiser_find = form.cleaned_data.get('advertiser')
            advertiser = Advertiser.objects.get(advertiser_id=advertiser_find)
            ad = Ad(title=form.cleaned_data.get('title'), link=form.cleaned_data.get('link'),
                    image=form.cleaned_data.get('image'), advertiser=advertiser)
            ad.save()
            return HttpResponseRedirect('/ads/show/')
        except:
            raise Http404('the error is in finding advertiser')


class ShowDetails(TemplateView):
    template_name = 'Advertiser_management/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list_of_ad = Ad.objects.all()
        result = {}
        for ad_element in list_of_ad:
            hour_and_clicks = {}
            list_of_hours = Click.objects.filter(ad=ad_element).order_by('time__hour').values('time__hour')
            for i in list_of_hours:
                list_of_ordered = Click.objects.filter(ad=ad_element).order_by('time__hour').values(
                    'time__hour').filter(time__hour=i['time__hour']).aggregate(Count('time'))
                number = list_of_ordered['time__count']
                time_hour = i['time__hour']
                hour_and_clicks[str(time_hour)] = str(number)
            result[ad_element] = hour_and_clicks
        context['result'] = result
        list_of_ad_reverse = Ad.objects.order_by('view__time').reverse().distinct('title','link')
        for a in list_of_ad_reverse:
            number_of_clicks =  Click.objects.filter(ad=a).annotate(Count())
        list_of_views = Ad.objects.order_by('title')
        for element in list_of_views:
            View.objects.filter(ad=element)
            Click.objects.filter(ad=element)

        return context




