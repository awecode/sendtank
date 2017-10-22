from rest_framework import serializers

from .models import List, Campaign, Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'short_name', 'full_name', 'first_name', 'middle_name', 'last_name', 'email', 'phone')


class ListSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['company'] = self.context['request'].company
        return super().create(validated_data)

    class Meta:
        model = List
        fields = ('id', 'name',)


class ListDetailSerializer(serializers.ModelSerializer):
    customers = CustomerSerializer(many=True)

    class Meta:
        model = List
        fields = ('id', 'name', 'customers')


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('id', 'name', 'list')
