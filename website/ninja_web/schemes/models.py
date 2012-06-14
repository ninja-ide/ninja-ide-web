# encoding: utf-8
from datetime import date

#from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models

from tagging.fields import TagField
from tagging.models import Tag


class Scheme(models.Model):
    """
    Model to keep the information about NINJA-IDE schemes uploaded by the
    community from our website.
    """

    user = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length="100", verbose_name=(u'scheme name'))
    upload_date = models.DateField(default=date.today)
    scheme_file = models.FileField(upload_to='schemes/')

    tags = TagField()

    def __unicode__(self):
        return u'%s' % self.name

    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    @models.permalink
    def get_absolute_url(self):
        return ('scheme_detail', (), {'scheme_id': self.id})
