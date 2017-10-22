from rest_framework import serializers

from .models import List, Campaign


class ListSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['company'] = self.context['request'].company
        return super().create(validated_data)

    class Meta:
        model = List
        fields = ('id', 'name',)


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('name',)
