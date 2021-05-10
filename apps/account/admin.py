from django.contrib import admin

from apps.account.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name')


admin.site.register(User, UserAdmin)
