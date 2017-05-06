from django.contrib import admin
from .models import SiteUser


class SiteUserModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'date_joined']

admin.site.register(SiteUser, SiteUserModelAdmin)
