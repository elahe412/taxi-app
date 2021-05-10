from django.contrib import admin

from apps.driver.models import Driver


class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','status')


admin.site.register(Driver, DriverAdmin)
