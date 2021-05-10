from django.contrib import admin


from apps.driver.models import Driver
from apps.passenger.models import Passenger


class PassengerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','status')


admin.site.register(Passenger, PassengerAdmin)
