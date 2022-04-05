from datetime import datetime
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    birthday = models.DateField(null=True, blank=True)

    objects = UserManager()

    unique_fields = (email, )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return f'{self.name} {self.last_name}'

    @property
    def age(self):
        """Get the model's age

        Returns:
            int: User's age
        """
        now = datetime.now()
        age = None

        if (self.birthday):
            birth = datetime(year=self.birthday.year, month=self.birthday.month, day=self.birthday.day)
            age = (now - birth).days // 365

        return age

    def __str__(self):
        return self.email
