from rest_framework.decorators import api_view, list_route
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import viewsets

from apps.users.models import Role
from apps.users.serializers import RoleSerializer


class RoleViewSet(viewsets.GenericViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

    @list_route(methods=['POST'])
    def switch(self, request):
        try:
            role = Role.objects.get(request.data.get('id'), user=request.user)
            request.session['role'] = role.id
            return Response(RoleSerializer(role).data)
        except Role.DoesNotExist:
            raise APIException('Invalid role')
