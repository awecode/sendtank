from django.db import models

from apps.users.models import Company


class List(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    list = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
