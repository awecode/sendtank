from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils import timezone


class User(AbstractBaseUser):
    email = models.EmailField(blank=True, unique=True)
    full_name = models.CharField(max_length=245)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_superuser
