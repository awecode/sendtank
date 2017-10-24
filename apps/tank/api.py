from rest_framework import viewsets

from .serializers import ListSerializer, CampaignSerializer, ListDetailSerializer, CustomerSerializer
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


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = CustomerSerializer
