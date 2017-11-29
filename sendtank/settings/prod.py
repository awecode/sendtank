from .base import *

ALLOWED_HOSTS = ['sendtank.com', ]

OPBEAT = {
    'ORGANIZATION_ID': '463c8be84d4e4dfeb1e5feca945b5998',
    'APP_ID': '5cf1db50e0',
    'SECRET_TOKEN': '66633d40a419436743afcac979e302c1b004c4ee',
}

MIDDLEWARE += [
    'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
]
