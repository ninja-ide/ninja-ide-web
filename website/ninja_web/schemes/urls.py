# -*- coding: utf-8 *-*
from django.conf.urls.defaults import patterns, url

from schemes.api import get_schemes_dict
from schemes.views import (scheme_submit, get_scheme, schemes, scheme_edit)


# VIEWS
urlpatterns = patterns('schemes.views',
    url(r'^edit/(?P<scheme_id>\d+)/$', scheme_edit, name="scheme_edit"),
    url(r'^submit/$', scheme_submit, name="scheme_submit"),
    url(r'^(?P<scheme_id>\d+)/$', get_scheme, name="scheme_detail"),
    url(r'^$', schemes, name="schemes"),
)

# API
urlpatterns += patterns('schemes.api',
    url(r'^api/$', get_schemes_dict),
)
