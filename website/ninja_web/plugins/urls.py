# -*- coding: utf-8 *-*
from django.conf.urls.defaults import patterns, url
from plugins.views import (plugin_submit, get_plugin, plugins, plugin_edit,
                           get_plugins_dict, get_schemes_dict)


urlpatterns = patterns('plugins.views',
    # from common.views
    url(r'^official/$', get_plugins_dict, {'query': 'official'}),
    url(r'^community/$', get_plugins_dict, {'query': 'community'}),
    url(r'^schemes/$', get_schemes_dict),

    # from plugins.views
    url(r'^edit/(?P<plugin_id>\d+)/$', plugin_edit, name="plugin_edit"),
    url(r'^submit/$', plugin_submit, name="plugin_submit"),
    url(r'^(?P<plugin_id>\d+)/$', get_plugin, name="plugin_detail"),
    url(r'^$', plugins, name="plugins"),
)
