from django.contrib.postgres.fields import ArrayField
from django.db import models

from apps.send.models import CHANNELS, Channel
from apps.users.models import Company


class List(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='lists')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='campaigns')
    channels = ArrayField(models.CharField(choices=CHANNELS, max_length=255), blank=True, null=True, default=['HousedSMS'])
    template = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def company(self):
        return self.list.company

    def trigger(self):
        for channel_name in self.channels:
            channel = Channel.get(channel_name)
            channel.trigger(self)

    def __str__(self):
        return self.name


# class Trigger(models.Model):
#     campaign = models.ForeignKey(Campaign, related_name='triggers')
#     type = models.CharField(default='Manual')
#     created_at = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = ArrayField(models.EmailField(blank=True, null=True), blank=True, null=True)
    phone = ArrayField(models.CharField(max_length=100, blank=True, null=True), blank=True, null=True)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='customers')
    lists = models.ManyToManyField(List, related_name='customers', through='ListCustomer')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def name(self):
        st = self.full_name or ''
        if not st and (self.first_name or self.middle_name or self.last_name):
            return ('%s %s %s' % (self.first_name or '', self.middle_name or '', self.last_name or '')).strip().replace(' ', ' ')
        return st or str(self.email) or str(self.phone) or ''

    @property
    def short_name(self):
        return self.first_name or self.name.split(' ')[0]

    def __str__(self):
        return self.name


class ListCustomer(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s  - %s' % (self.list, self.customer)

    class Meta:
        auto_created = True
