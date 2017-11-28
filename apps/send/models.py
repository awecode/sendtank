from django.db import models

from fcm.models import AbstractDevice

from ..users.models import User


# Base Channel class
class Channel(object):
    name = None

    @staticmethod
    def get(name):
        return dict(CHANNELS).get(name)

    def __init__(self):
        if not self.name:
            raise NotImplemented('Channel should have a name')


class HousedSMS(Channel):
    name = 'HousedSMS'

    @classmethod
    def trigger(klass, campaign):
        # todo do this in company model
        roles = campaign.list.company.roles.all()
        # users = []
        for role in roles:
            role.user.send_push({'campaign': campaign.id})
            # users.append(role.user)
            # users = set(users)
            # send fcm notification


CHANNELS = (
    ('HousedSMS', HousedSMS),
)


class UserDevice(AbstractDevice):
    user = models.ForeignKey(User, related_name='devices', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def send_all(cls, msg):
        cls.objects.filter(is_active=True).send_message(msg)

    def __str__(self):
        return 'FCM Device for %s' % self.user
