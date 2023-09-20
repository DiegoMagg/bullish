from accounts import models
from django.contrib import admin


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass
