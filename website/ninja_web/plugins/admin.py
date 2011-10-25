# -*- coding: utf-8 *-*
from django.contrib import admin

from plugins.models import Plugin
from plugins.models import Vote


class PluginAdmin(admin.ModelAdmin):
    pass
admin.site.register(Plugin, PluginAdmin)


class VoteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Vote, VoteAdmin)
