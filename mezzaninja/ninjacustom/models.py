from django.db import models

from mezzanine.pages.models import Page
from mezzanine.core.models import Orderable, RichText

OS_CHOICES = (
    ('linux', 'Linux'),
    ('win', 'Windows'),
    ('mac', 'Mac'),
    ('source', 'Source'),
)


class LinksPage(Page, RichText):
    """
    A page that would contain a lot of links
    """
    class Meta:
        verbose_name = "Links Page"
        verbose_name_plural = "Links Pages"


class DownloadLink(Orderable):
    """
    Link that could be inserted in a LinksPage page.
    """
    page = models.ForeignKey("LinksPage", related_name="download_links")
    link = models.URLField("URL", max_length=200)
    version = models.CharField("Version", max_length=20, blank=True)
    os = models.CharField("OS", choices=OS_CHOICES, max_length=10)
    distribution = models.CharField("OS Distribution/Version",
                                    max_length=80, blank=True)
    extra_detail = models.CharField("Detail", max_length=800, blank=True)


class TeamPage(Page, RichText):
    class Meta:
        verbose_name = "Team Page"


class TeamMember(Orderable):
    page = models.ForeignKey("TeamPage", related_name="team_members")
    name = models.CharField("Name", max_length=200)
    irc_nickname = models.CharField("IRC NickName", max_length=200)
    twitter = models.CharField("Twitter", max_length=300,
                               help_text='Just the user', blank=True)
    email = models.EmailField("Email", max_length=200, blank=True)
    detail = models.TextField("Detail", blank=True)
    web = models.URLField("Some web of him/her", max_length=200, blank=True)
