from django.db import models

class Tip(models.Model):
	""" Tips to show in the page.
		`text` is the text to be shown with autoescape off, so
		links are allowed.
		`datetime_since` date since when will be available
		`datetime_until` date since won't be available
	"""
	text = models.TextField()
	has_links = models.BooleanField(default=False, help_text=u'Needed for escaping characters')
	datetime_since = models.DateTimeField(auto_now_add=True, help_text=u'Since when is available for publishing')
	datetime_until = models.DateTimeField(help_text=u'Date until it is viewable')
	container_class = models.TextField(max_length=50, help_text=u'HTML class for the wrapper')

	def __unicode__(self):
		return u'%s...' % text[30:]
