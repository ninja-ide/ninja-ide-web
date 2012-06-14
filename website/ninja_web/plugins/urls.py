# -*- coding: utf-8 *-*
from django.conf.urls.defaults import patterns, url

from plugins.api import get_plugins_dict
from plugins.views import plugin_submit, get_plugin, plugins, plugin_edit


# VIEWS
urlpatterns = patterns('plugins.views',
    url(r'^edit/(?P<plugin_id>\d+)/$', plugin_edit, name="plugin_edit"),
    url(r'^submit/$', plugin_submit, name="plugin_submit"),
    url(r'^(?P<plugin_id>\d+)/$', get_plugin, name="plugin_detail"),
    url(r'^$', plugins, name="plugins"),
)

# API
urlpatterns += patterns('plugins.api',
    url(r'^api/official/$', get_plugins_dict, {'query': 'official'}),
    url(r'^api/community/$', get_plugins_dict, {'query': 'community'}),
    url(r'^api/(?P<query>\w+)/$', get_plugins_dict),
    url(r'^api/$', get_plugins_dict),
)
