from apps.users.models import Role
from rest_framework.authtoken.models import Token

from apps.users.serializers import RoleSerializer


def clear_roles(request):
    request.__class__.role = None
    request.__class__.company = None
    request.__class__.roles = []
    request.__class__.role_data = []
    return request


class RoleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.META.get('HTTP_AUTHORIZATION'):
            token_key = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
            try:
                request.user = Token.objects.get(key=token_key).user
            except Token.DoesNotExist:
                pass

        role = None
        if request.user.is_authenticated:
            roles = list(Role.objects.filter(user=request.user).select_related('company'))
            if request.session.get('role'):
                role = next((role for role in roles if role.id == request.session.get('role')), None)
            if not role and roles:
                role = roles[0]
            if role:
                request.__class__.role = role
                request.__class__.company = role.company
                request.__class__.roles = roles
                request.__class__.role_data = RoleSerializer(roles, many=True, active=role).data
        if not role:
            request = clear_roles(request)

        response = self.get_response(request)
        return response
