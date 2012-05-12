# -*- coding: utf-8 *-*
from django.http import HttpResponse

from plugins.models import Plugin

try:
    import json
except ImportError:
    import simplejson as json


def community_plugins(request):
    """ Returns the list of plugins uploaded by the community with metadata
    """
    plugins_list = Plugin.objects.all()
    return _gather_plugings_json(plugins_list)


def official_plugins(request):
    """ Returns the list of plugins uploaded by the community with metadata
    """
    plugins_list = Plugin.objects.filter(user__is_superuser=True,
                                         user__is_staff=True)
    return _gather_plugings_json(plugins_list)


def _gather_plugings_json(plugins_list):
    """ Given a QuerySet of plugins, returns them in a json with metadata
    """
    plugins = []

    for plugin in plugins_list:
        plugin_data = {}
        plugin_data['name'] = plugin.name
        plugin_data['description'] = plugin.description
        plugin_data['version'] = "0.1"

        plugin_data['download'] = plugin.zip_file.url
        plugin_data['home'] = plugin.get_absolute_url()
        plugin_data['authors'] = plugin.user.username

        plugins.append(plugin_data)

    return HttpResponse(json.dumps(plugins), mimetype="application/json")


# For now, I decided to consider color schemes as plugins. We should discuss
# this.
def schemes(request):
    return render_response(request, 'schemes.html')
