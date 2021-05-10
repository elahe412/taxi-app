# import random
#
# from apps.account.models import User
# from apps.trip.models import Trip
#
#
# def choose_driver(self):
#     bussy_drivers = Trip.objects.values_list('driver', flat=True)
#     all_drivers = User.objects.filter(role='d')
#     allowed = [drv for drv in all_drivers if drv not in bussy_drivers]
#     selected_driver = random.choice(allowed)
#     return selected_driver.id
