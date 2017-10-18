from rest_framework.decorators import list_route
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Role, User
from .serializers import RoleSerializer, UserSerializer


def check_required_fields(data, required_fields):
    for field in required_fields.keys():
        if not data.get(field):
            raise APIException('%s field is required.' % required_fields.get(field))


class RoleViewSet(viewsets.GenericViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

    @list_route(methods=['POST'])
    def switch(self, request):
        try:
            role = Role.objects.get(id=request.data.get('id'), user=request.user)
            request.session['role'] = role.id
            return Response(RoleSerializer(role).data)
        except Role.DoesNotExist:
            raise APIException('Invalid role')


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @list_route(methods=['POST'])
    def login(self, request):
        data = request.data
        required_fields = {
            'username': 'Username',
            'password': 'Password',
        }
        check_required_fields(data, required_fields)
