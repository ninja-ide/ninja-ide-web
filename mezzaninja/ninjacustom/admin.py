from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin

from .models import DownloadLink, LinksPage, TeamPage, TeamMember


class DownloadLinkInline(TabularDynamicInlineAdmin):
    model = DownloadLink


class LinksPageAdmin(PageAdmin):
    inlines = (DownloadLinkInline,)

admin.site.register(LinksPage, LinksPageAdmin)


class TeamMemberInline(TabularDynamicInlineAdmin):
    model = TeamMember


class TeamPageAdmin(PageAdmin):
    inlines = (TeamMemberInline,)

admin.site.register(TeamPage, TeamPageAdmin)
