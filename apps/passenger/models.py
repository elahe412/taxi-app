from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from apps.account.models import User


class Passenger(User):
    user = models.OneToOneField(to=User, parent_link=True, related_name='passenger', on_delete=models.CASCADE)
    status = models.CharField(max_length=20,
                              choices=(('waiting_for_driver', 'waiting_for_driver'), ('busy', 'busy'),
                                       ('free', 'free')))

    def __str__(self):
        return super(Passenger, self).__str__()
