# -*- coding: utf-8 *-*
import datetime

from django.contrib.auth.models import User
from django.views.generic import DetailView, TemplateView


class CountdownTemplateView(TemplateView):
    template_name = 'baseCountdown.html'

    def get_context_data(self):
        diff = datetime.datetime(2011, 9, 23) - datetime.datetime.today()
        time_left = "0{0}:{1}:{2}:{3}".format(
            diff.days,
            diff.seconds / 60 / 60,
            diff.seconds / 60 - (diff.seconds / 60 / 60 * 60),
            diff.seconds - (diff.seconds / 60 * 60)
        )
        return {'time_left': time_left}


class UserDetailView(DetailView):
    """ Returns the user (as 'page_user') info and his/her plugins
        Nothing in case error or no existing user
    """
    model = User
    slug_url_kwarg = 'user_name'
    template_name = 'user_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = {}
        try:
            user = User.objects.get(username=kwargs['user_name'])
            context['user_page'] = user
        except User.DoesNotExist:
            pass
        else:
            user_plugins = user.plugin_set.all()
            context['plugins'] = user_plugins
            context['user_submitted_plugins'] = user_plugins.exists()
        return context
