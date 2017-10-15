from django.contrib.postgres.fields import ArrayField
from django.db import models

from apps.send.models import CHANNELS
from apps.users.models import Company


class List(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    channels = ArrayField(models.CharField(choices=CHANNELS, max_length=255), blank=True, null=True)

    @property
    def company(self):
        return self.list.company

    def __str__(self):
        return self.name
