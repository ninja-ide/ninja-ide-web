# encoding: utf-8
from datetime import date
from decimal import Decimal

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg

from tagging.fields import TagField
from tagging.models import Tag


class Plugin(models.Model):
    """
    Model to keep the information about NINJA-IDE plugins uploaded by the
    community from our website.
    """
    user = models.ForeignKey(User, blank=True, null=True)

    name = models.CharField(max_length="100", verbose_name=(u'Plugin name'))
    short_description = models.CharField(
                            max_length=100, verbose_name=u'Short Description')
    description = models.TextField(verbose_name=u'Description')
    upload_date = models.DateField(default=date.today)
    url = models.URLField(verify_exists=True, max_length=200, blank=True)

    zip_file = models.FileField(upload_to='plugin_files/')

    tags = TagField()

    def __unicode__(self):
        return u'Plugin name: %s | Uploaded by: %s' % \
                                            (self.name, self.user.username)

    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    @property
    def rate(self):
        """ return the actual average rate rounded 
        """
        if self.vote_set.all().count() == 0:
            # default value for non rated plugins
            avg = 2.5
        else:
            dummy = self.vote_set.aggregate(Avg('rate'))
            avg = Decimal(str(dummy['rate__avg'])).quantize(Decimal("0.01"))
        return avg

    @property
    def rate_times(self):
        return self.vote_set.all().count()

    @models.permalink
    def get_absolute_url(self):
        return reverse('plugins.views.plugin', None, {'plugin_id': self.id})


class Vote(models.Model):
    """ Represents the vote that a user gave to a plugin.
        Default rate is the middle of 0 and 5 (min & max values)
    """
    user = models.ForeignKey(User)
    plugin = models.ForeignKey(Plugin)
    rate = models.DecimalField(decimal_places=2, max_digits=3, default=2.50)
    date = models.DateField(default=date.today)
    voter_ip = models.IPAddressField()

    class Meta:
        unique_together = ('plugin', 'user',)

    def __unicode__(self):
        return u'Vote for plugin: %s | Voter: %s | Rate: %d.' % \
                                (self.plugin, self.user.username, self.rate)
