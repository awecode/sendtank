from django.db import models


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
    
    def trigger(self, campaign):
        pass
        # send fcm notification
        


CHANNELS = (
    ('HousedSMS', HousedSMS),
)
