from rest_framework import serializers
from .models import Advertiser,Ad,Click,View

class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = '__all__'
    def create(self, validated_data):
        advertiser = Advertiser(name=validated_data['name'],advertiser_id=validated_data['advertiser_id'])
        advertiser.save()
        return advertiser
class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
    def create(self, validated_data):
        ad = Ad(title=validated_data['title'],link=validated_data['link'],image=validated_data['image'],advertiser=validated_data['advertiser'],approve=validated_data['approve'])
        ad.save()
        return ad
class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = '__all__'
    def create(self, validated_data):
        click = Click(ad=validated_data['ad'],time=validated_data['time'],user_id=validated_data['user_id'])
        click.save()
        return click
class ViewSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        view = View(time=validated_data['time'],ad=validated_data['ad'],user_id=validated_data['user_id'])
        view.save()
        return view
    class Meta:
        model = View
        fields = '__all__'
