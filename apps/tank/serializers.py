from rest_framework import serializers

from .models import List, Campaign


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('name',)


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('name',)
