from django import forms
class data_form(forms.Form):
    title = forms.CharField(max_length=200,label='title')
    link = forms.CharField(max_length=200,label='link')
    img_url = forms.CharField(max_length=200,label='img')
    advertiser_id = forms.IntegerField(label='advertiser')