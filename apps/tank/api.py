from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .serializers import ListSerializer, CampaignSerializer, ListDetailSerializer, CustomerSerializer, CampaignDetailSerializer
from .models import List, Campaign, Customer


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all().order_by('-id')
    serializer_class = ListSerializer
    detail_serializer_class = ListDetailSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return self.serializer_class


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all().order_by('-id')
    serializer_class = CampaignSerializer

    # todo change to post
    @detail_route(methods=['get'])
    def trigger(self, request, pk=None, format=None):
        campaign = get_object_or_404(Campaign, pk=pk)
        campaign.trigger()
        return Response({})

    @detail_route(methods=['get'])
    def details(self, request, pk=None, format=None):
        campaign = get_object_or_404(Campaign.objects.prefetch_related('list__customers'), pk=pk)
        serializer = CampaignDetailSerializer(campaign)
        return Response(serializer.data)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = CustomerSerializer
