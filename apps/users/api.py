from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import list_route
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .models import Role, User
from .serializers import RoleSerializer, UserSerializer


def check_required_fields(data, required_fields):
    for field in required_fields.keys():
        if not data.get(field):
            raise ValidationError({field: ['%s is required.' % required_fields.get(field)]})


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
            raise ValidationError('Invalid role')


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = ()
    authentication_classes = ()

    @list_route(methods=['POST'])
    def login(self, request):
        data = request.data
        required_fields = {
            'email': 'Email',
            'password': 'Password',
        }
        check_required_fields(data, required_fields)
        user = authenticate(username=data.get('email'), password=data.get('password'))
        if user:
            login(request, user)
            all_roles = user.all_roles
            return Response({'user': user.data, 'roles': RoleSerializer(all_roles, many=True, active=all_roles[0]).data})
        else:
            raise ValidationError({'__form__': ['Invalid email or password']})

    @list_route(methods=['POST'])
    def logout(self, request):
        logout(request)
        return Response({})


class CustomObtainAuth(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_data = UserSerializer(user, many=False).data
        user_data['token'] = token.key
        return Response(user_data)
