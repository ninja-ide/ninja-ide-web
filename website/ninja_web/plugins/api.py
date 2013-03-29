# -*- coding: utf-8 *-*
from django.db.models import Q
from django.http import HttpResponse
from django.utils.safestring import SafeString

from plugins.models import Plugin

try:
    import json
except ImportError:
    import simplejson as json


def get_plugins_dict(request, query=None):
    """ Returns the list of plugins with metadata.
        Depending on 'query' the returned json will contain matching plugins

        @query: 'official'|'community'|<query_string>|None

        In case some query_string is provided it will use it as query and will
        lookup plugins with that string in name, decription and authors.
    """

    plugins = []  # dict to return
    plugins_list = Plugin.objects.all()  # initial query

    if query is not None:
        if query == 'community':
            plugins_list = plugins_list.filter(user__is_staff=False)
        elif query == 'official':
            plugins_list = plugins_list.filter(user__is_staff=True)
        else:
            if len(query) > 2:
                # if string should be used as lookup string we look for query
                plugins_list = plugins_list.filter(Q(name__icontains=query)\
                                                 | Q(description__icontains=query)\
                                                 | Q(user__username__icontains=query)\
                                                 | Q(tags__icontains=query))

    for plugin in plugins_list:
        plugin_data = {}
        plugin_data['name'] = plugin.name
        plugin_data['description'] = SafeString(u'%s') % plugin.description
        plugin_data['version'] = plugin.version or u'N/A'
        plugin_data['download'] = request.build_absolute_uri(plugin.zip_file.url)
        plugin_data['tags'] = plugin.tags.split() or []
        plugin_data['rate'] = '%.2f' % plugin.rate
        plugin_data['home'] = plugin.get_absolute_url()
        plugin_data['authors'] = plugin.user.get_full_name() or plugin.user.username

        plugins.append(plugin_data)

    # this kind of return enables to print non ascii characters
    return HttpResponse(json.dumps(plugins, ensure_ascii=False),
                        mimetype="application/json;charset=UTF-8")
