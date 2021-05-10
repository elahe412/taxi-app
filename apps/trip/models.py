import random

from django.db import models

from apps.driver.models import Driver
from apps.passenger.models import Passenger



class Trip(models.Model):
    destination = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    driver = models.ForeignKey(Driver, related_name='trip', on_delete=models.CASCADE, null=True, blank=True)
    passenger = models.ForeignKey(Passenger, related_name='trips', on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField(default=15000)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    STATUS = (
        ('REQUESTED', 'REQUESTED'),
        ('IN_PROGRESS', 'IN_PROGRESS'),
        ('COMPLETED', 'COMPLETED'),
    )
    status = models.CharField(max_length=11, choices=STATUS, default='')
