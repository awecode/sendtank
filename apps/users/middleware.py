from apps.users.models import Role
from rest_framework.authtoken.models import Token


def clear_roles(request):
    request.__class__.role = None
    request.__class__.company = None
    request.__class__.group = None
    request.__class__.roles = []
    request.__class__.is_owner = False
    # request.__class__.groups = []
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

        if request.user.is_authenticated:
            role = None
            if request.session.get('role'):
                try:
                    role = Role.objects.select_related('company').get(pk=request.session.get('role'), user=request.user)
                except Role.DoesNotExist:
                    pass

            if not role:
                roles = Role.objects.filter(user=request.user).select_related('company')
                if roles:
                    role = roles[0]
                    request.session['role'] = role.id
            if role:
                request.__class__.role = role
                request.__class__.company = role.company
                request.__class__.roles = Role.objects.filter(user=request.user)
            else:
                request = clear_roles(request)
        else:
            request = clear_roles(request)

        response = self.get_response(request)
        return response
