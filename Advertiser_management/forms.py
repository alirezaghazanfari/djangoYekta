from django import forms
class data_form(forms.Form):
    title = forms.CharField(max_length=200,label='title')
    link = forms.CharField(max_length=200,label='link')
    image = forms.URLField(max_length=200,label='image')
    advertiser = forms.IntegerField(label='advertiser')