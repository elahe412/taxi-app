# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from apps.driver.models import Driver
#
#
# @receiver(post_save, sender=Driver)
# def save_profile(sender, instance, created, **kwargs):
#     if created:
#         User.objects.create(username=instance)
#
# #