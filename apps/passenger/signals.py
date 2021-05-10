# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from apps.passenger.models import Passenger
#
#
# @receiver(post_save, sender=User)
# def post_save_create_profile(sender, instance, created, **kwargs):
#     if created:
#         Passenger.objects.create(user=instance)
