from django.contrib.postgres.fields import ArrayField
from django.db import models

from apps.send.models import CHANNELS
from apps.users.models import Company


class List(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    channels = ArrayField(models.CharField(choices=CHANNELS, max_length=255), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def company(self):
        return self.list.company

    def __str__(self):
        return self.name


class Customer(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = ArrayField(models.EmailField(blank=True, null=True), blank=True, null=True)
    phone = ArrayField(models.CharField(max_length=100, blank=True, null=True), blank=True, null=True)
    lists = models.ManyToManyField(List, related_name='customers', through='ListCustomer')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def name(self):
        st = self.full_name or ''
        if not st and (self.first_name or self.middle_name or self.last_name):
            return '%s %s %s' % (self.first_name, self.middle_name, self.last_name).strip().replace(' ', ' ')
        return self.email or self.phone or ''

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
