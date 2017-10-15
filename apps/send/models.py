from django.db import models


# Base Channel class
class Channel(object):
    name = None

    def __init(self):
        if not self.name:
            raise NotImplemented('Channel should have a name')


class HousedSMS(Channel):
    name = 'HousedSMS'


channels = (
    ('HousedSMS', HousedSMS),
)
