# -*- coding: utf-8 *-*
import datetime

from django.http import HttpResponse
from django.contrib.auth.models import User

from common.utils import render_response
from plugins.models import Plugin


try:
    import json
except ImportError:
    import simplejson as json

def countdown(request):
    diff = datetime.datetime(2011, 9, 23) - datetime.datetime.today()
    time_left = "0{0}:{1}:{2}:{3}".format(
        diff.days,
        diff.seconds / 60 / 60,
        diff.seconds / 60 - (diff.seconds / 60 / 60 * 60),
        diff.seconds - (diff.seconds / 60 * 60)
    )
    return render_response(request, 'baseCountdown.html',
                                        {'time_left': time_left})


def intro(request):
    """ Intro/Splash screen.
    """
    return render_response(request, 'intro.html')


def features(request):
    """ Features section.
    """
    return render_response(request, 'features.html')


def downloads(request):
    """ Downloads section.
    """
    return render_response(request, 'downloads.html')


def about(request):
    """ About section. All ninja people: devs and packagers
    """
    return render_response(request, 'about.html')


def using(request):
    """ People using Ninja-ide.
    """
    return render_response(request, 'using.html')


def contrib(request):
    """ Contribution section. All info to do so.
    """
    return render_response(request, 'contrib.html')


# plugins

def schemes(request):
    return render_response(request, 'schemes.html')


def oficial(request):
    return render_response(request, 'oficial.html')


def official(request):
    return render_response(request, 'oficial.html')


def community(request):
    """ Returns the list of plugins with metadata
    """
    plugins_list = Plugin.objects.all()
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


def updates(request):
    """ Just returns a simple json formatted file telling the 
        actual and stable ninja-ide version. 
    """
    return render_response(request, 'updates_simple.html')


def user_detail(request, user_name=None):
    """ Returns the user (as 'page_user') info and his/her plugins
        Nothing in case error or no existing user
    """
    dicc = {}

    try:
        user = User.objects.get(username=user_name)
        dicc['user_page'] = user
    except Exception, e:
        print e
    else:
        dicc['plugins'] = user.plugin_set.all()

    return render_response(request, 'user_detail.html', dicc)

