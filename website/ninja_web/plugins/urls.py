# -*- coding: utf-8 *-*
from django.conf.urls.defaults import patterns, url

from plugins.api import (schemes, official_plugins, community_plugins)
from plugins.views import (plugin_submit, get_plugin, plugins, plugin_edit)


urlpatterns = patterns('plugins.views',
    url(r'^edit/(?P<plugin_id>\d+)/$', plugin_edit, name="plugin_edit"),
    url(r'^submit/$', plugin_submit, name="plugin_submit"),
    url(r'^(?P<plugin_id>\d+)/$', get_plugin, name="plugin_detail"),
    url(r'^$', plugins, name="plugins"),
)

urlpatterns += patterns('plugins.api',

    # API
    url(r'^community/', community_plugins),
    url(r'^official/', official_plugins),

    url(r'^schemes', schemes),
)
