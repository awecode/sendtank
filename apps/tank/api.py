from rest_framework import viewsets

from .serializers import ListSerializer, CampaignSerializer, ListDetailSerializer
from .models import List, Campaign


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    detail_serializer_class = ListDetailSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return self.serializer_class


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
