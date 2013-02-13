# -*- coding: utf-8 *-*
from django.db import models


class DownloadUrl(models.Model):
    """
    Little model to keep the information about NINJA-IDE download URLs.
    """
    os = models.CharField(max_length="100", verbose_name=(u'Operative System'))
    url = models.URLField(verbose_name=(u'Download URL'))

    def __unicode__(self):
        return u'Download URL for %s' % (self.os, )


class PeopleUsing(models.Model):
    name = models.CharField(max_length=300)
    website = models.URLField(verbose_name=(u'Download URL'), blank=True)
    logo = models.ImageField(upload_to="using/")
    brief = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % self.name
