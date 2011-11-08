# -*- coding: utf-8 *-*
import datetime

from common.utils import render_response


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
    return render_response(request, 'intro.html')


def features(request):
    return render_response(request, 'features.html')


def downloads(request):
    return render_response(request, 'downloads.html')


def about(request):
    return render_response(request, 'about.html')


def using(request):
    return render_response(request, 'using.html')


def contrib(request):
    return render_response(request, 'contrib.html')


# plugins

def plugins_contest(request):
    return render_response(request, 'plugins-contest.html')


def schemes(request):
    return render_response(request, 'schemes.html')


def oficial(request):
    return render_response(request, 'oficial.html')


def official(request):
    return render_response(request, 'oficial.html')


def community(request):
    return render_response(request, 'community.html')

def updates(request):
    return render_response(request, '404.html')
