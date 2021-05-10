import random

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from apps.account.models import User


class RandomDriverManager(models.Manager):
    def get_random_driver(self):
        drivers = self.filter(status='waiting')
        if drivers:
            random_driver = random.choice(drivers)
            return random_driver
        else:
            return False


class Driver(User):
    user = models.OneToOneField(to=User, parent_link=True, related_name='driver', on_delete=models.CASCADE)
    national_code = models.CharField(max_length=10)
    status = models.CharField(max_length=20,default='waiting',
                              choices=(('waiting', 'waiting'), ('busy', 'busy'),
                                       ('toward_the_passenger', 'toward_the_passenger')))

    def __str__(self):
        return super(Driver, self).__str__()

    random = RandomDriverManager()


