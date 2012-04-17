# -*- coding: utf-8 *-*
from django.conf.urls.defaults import patterns, url
from plugins.views import (plugin_submit, plugin, plugins)
from common.views import (schemes, official, community)


urlpatterns = patterns('plugins.views',
    # from common.views
    url(r'^schemes', schemes),
    url(r'^official', official),
    url(r'^community', community),

    # from plugins.views
    url(r'^submit/$', plugin_submit, name="plugin_submit"),
    url(r'^(?P<plugin_id>\d+)/$', plugin, name="plugin_detail"),
    url(r'^$', plugins, name="plugins"),
)
