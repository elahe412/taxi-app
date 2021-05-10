from rest_framework import permissions

from apps.driver.models import Driver


class DriversPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user in Driver.objects.all()
