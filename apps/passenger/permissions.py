from rest_framework import permissions

from apps.passenger.models import Passenger


class PassengersPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user in Passenger.objects.all()
