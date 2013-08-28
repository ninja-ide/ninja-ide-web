# -*- coding: utf-8 *-*
from django.conf.urls import patterns, url

from plugins.api import get_plugins_dict
from plugins.views import plugin_submit
from plugins.views import (PluginDetailView,
                           PluginListView,
                           PluginEditView)


# VIEWS
urlpatterns = patterns(
    'plugins.views',

    url(r'^edit/(?P<plugin_id>\d+)/$',
        PluginEditView.as_view(),
        name="plugin_edit"),

    url(r'^submit/$',
        plugin_submit,
        name="plugin_submit"),

    url(r'^(?P<plugin_id>\d+)/$',
        PluginDetailView.as_view(),
        name="plugin_detail"),

    url(r'^$',
        PluginListView.as_view(),
        name="plugin_list"),
)

# API
urlpatterns += patterns(
    'plugins.api',

    # URLs for existing/old versions
    url(r'^official/$',
        get_plugins_dict,
        {'query': 'official'}),

    url(r'^community/$',
        get_plugins_dict,
        {'query': 'community'}),

    url(r'^api/official/$',
        get_plugins_dict,
        {'query': 'official'}),

    url(r'^api/community/$',
        get_plugins_dict,
        {'query': 'community'}),

    url(r'^api/(?P<query>\w+)/$',
        get_plugins_dict),

    url(r'^api/$',
        get_plugins_dict),
)
