# -*- coding: utf-8 *-*
from django.contrib import admin

from common.models import DownloadUrl


class DownloadUrlAdmin(admin.ModelAdmin):
    list_display = ['os', 'url']
    list_filter = ['os', 'url']
    search_fields = ['os', 'url']
admin.site.register(DownloadUrl, DownloadUrlAdmin)
