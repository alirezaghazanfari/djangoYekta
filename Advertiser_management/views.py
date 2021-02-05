from datetime import timedelta

from django.db.models import Count
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView
from rest_framework.generics import ListCreateAPIView

from .forms import data_form
from .models import Ad, Advertiser, Click, View
from .serializers import AdvertiserSerializer


# Create your views here.
class ShowAdPageAPI(ListCreateAPIView):

    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer
    def list(self, request, *args, **kwargs):
        user_id_str = self.request.META.get('HTTP_X_FORWARDED_FOR')
        ip = ''
        list_of_ads = Ad.objects.all()
        if user_id_str:
            ip = user_id_str.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        for i in list_of_ads:
            i.inc_views(time=timezone.now(), user=ip)
            i.save()
        return super().list(request,*args,**kwargs)

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

        list_of_ad_for_report_2 = Ad.objects.all()
        dictionary_of_ad_rate = {}
        for ad_element in list_of_ad_for_report_2:
            number_of_clicks = Click.objects.filter(ad = ad_element).count()
            number_of_views = View.objects.filter(ad = ad_element).count()
            rate = number_of_clicks/number_of_views
            dictionary_of_ad_rate[ad_element] = rate
        sorted_list = (sorted(dictionary_of_ad_rate,key=dictionary_of_ad_rate.get,reverse=True))
        result2 = {}
        for a in sorted_list:
            result2[a] = dictionary_of_ad_rate.get(a)
        context['result2'] = result2


        user_id_dict =(Click.objects.values('user_id')).distinct()
        result_3 = {}
        for user_ip in user_id_dict:
            list_1 =   View.objects.filter(user_id = user_ip['user_id'])
            average = 0
            for view_time in list_1:
              time_click = Click.objects.filter(user_id = user_ip['user_id'],ad = view_time.ad).values_list('time')
              time_view = list_1.values_list('time')
              l =0
              for i in time_view:
                  try:
                    time2 = time_click[l][0]
                    time1 = i[0]
                    t1 = timedelta(hours=time1.hour,minutes=time1.minute,seconds=time1.second)
                    t2 = timedelta(hours=time2.hour, minutes=time2.minute, seconds=time2.second)
                    diff = (t2 - t1)
                    average+=diff.seconds
                    l+=1
                  except:
                    break
            number_2 =   View.objects.filter(user_id = user_ip['user_id']).count()
            average = average/number_2
            result_3[user_ip['user_id']] = average

        context['result3'] = result_3
        return context



def invertDictionary(d):
     myDict = {}
     for i in d:
       value = d.get(i)
       myDict.setdefault(value,[]).append(i)
     return myDict

