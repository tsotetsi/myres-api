from django.contrib import admin

from myres.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

