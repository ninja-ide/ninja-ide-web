# -*- coding: utf-8 *-*
from django.contrib import admin

from plugins.models import Plugin, Vote


class PluginAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'version', 'short_description',
                    'description', 'upload_date', 'url', 'zip_file', 'tags']
    list_filter = ['user', 'upload_date', 'tags']
    search_fields = ['user', 'name', 'short_description', 'description',
                     'upload_date', 'url', 'zip_file', 'tags']
admin.site.register(Plugin, PluginAdmin)


class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'plugin', 'rate', 'date', 'voter_ip']
    list_filter = ['user', 'plugin', 'rate', 'date', 'voter_ip']
    search_fields = ['user', 'plugin', 'rate', 'date', 'voter_ip']
admin.site.register(Vote, VoteAdmin)
