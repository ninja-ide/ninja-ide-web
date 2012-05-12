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
