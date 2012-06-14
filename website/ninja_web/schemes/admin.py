# -*- coding: utf-8 *-*
from django.contrib import admin

from schemes.models import Scheme


class SchemeAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'upload_date', 'tags']
    list_filter = ['tags']
    search_fields = ['user', 'name', 'upload_date', 'tags']
admin.site.register(Scheme, SchemeAdmin)
