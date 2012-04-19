# -*- coding: utf-8 *-*
from django.conf.urls.defaults import patterns, url
from plugins.views import (plugin_submit, get_plugin, plugins, plugin_edit)
from common.views import (schemes, official, community)


urlpatterns = patterns('plugins.views',
    # from common.views
    url(r'^schemes', schemes),
    url(r'^official', official),
    url(r'^community', community),

    # from plugins.views
    url(r'^edit/(?P<plugin_id>\d+)/$', plugin_edit, name="plugin_edit"),
    url(r'^submit/$', plugin_submit, name="plugin_submit"),
    url(r'^(?P<plugin_id>\d+)/$', get_plugin, name="plugin_detail"),
    url(r'^$', plugins, name="plugins"),
)
