from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, full_name='', password=None, active=True):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=UserManager.normalize_email(email),
            full_name=full_name,
        )
        if password:
            user.set_password(password)
        user.is_active = active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name='', password=None):
        user = self.create_user(
            email,
            password=password,
            full_name=full_name,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(blank=True, unique=True)
    full_name = models.CharField(max_length=245)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_superuser
