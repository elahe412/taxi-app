from django.contrib import admin

from apps.trip.models import Trip


class TripAdmin(admin.ModelAdmin):
    list_display = ('id','passenger','driver','status')


admin.site.register(Trip, TripAdmin)
