# encoding: utf-8
from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import simplejson
from django.views.generic import DetailView, ListView, UpdateView

from tagging.models import Tag

from common.utils import render_response
from .forms import PluginForm
from .models import Vote, Plugin

try:
    import json
except ImportError:
    import simplejson as json


class DecimalEncoder(simplejson.JSONEncoder):
    """JSON encoder which understands decimals."""
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

    def _iterencode(self, o, markers=None):
        if isinstance(o, Decimal):
            return (str(o) for o in [o])
        return super(DecimalEncoder, self)._iterencode(o, markers)


def filter_by_tag(request, tag_id):
    """
    Given a tag id, return all plugins with this tag.
    """
    tag = None
    context = {}

    try:
        tag = Tag.objects.get(id=tag_id)
        context['plugins_tag'] = tag.name
    except:
        pass
    else:
        context['plugins'] = Plugin.objects.filter(tags__icontains=tag.name)

    return render_response(request, 'plugins.html', context)


class PluginCreateView(UpdateView):
    pass


@login_required
def plugin_submit(request):
    context = {}

    form = PluginForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            new_plugin = form.save(commit=False)
            new_plugin.user = request.user
            new_plugin.save()
            messages.info(request,
                          u'Plugin submitted correctly little dragon.')

            return redirect('plugin_list')
        else:
            messages.error(
                request,
                u'Something went wrong in your submit. Please, check it.')

    context['form'] = form
    return render_response(request, 'plugin-submit.html', context)


@login_required
def rate_plugin(request):

    context = {}
    if request.method == 'GET':
        plugin_id = request.GET.get('plugin_id', False)
        rate = request.GET.get('rate', 0)

    if plugin_id and rate > 0:
        # plugin voted
        plugin = Plugin.objects.get(id=plugin_id)
        # the actual vote

        try:
            # if remote client is behind a proxy
            voter_ip = request.META['HTTP_X_FORWARDED_FOR'][0]
        except:
            # fallback for non 'proxies' clients
            voter_ip = request.META['REMOTE_ADDR']

        new_vote = Vote(plugin=plugin,
                        user=request.user,
                        rate=int(rate),
                        voter_ip=voter_ip,
                        )

        try:
            # este save tira un error por el unique together. Hay que cargar un
            # mensajito de error (el de ya votaste este plugin).
            new_vote.save()
            context['ok'] = True
            context['msg'] = u"Thanks for your vote!"

        except IntegrityError:
            #IntegrityError raises when tried to save violating
            # the unique_together Plugin meta.
            context['ok'] = False
            context['msg'] = u"You can't vote the same plugin twice!"

        except Exception, e:
            context['ok'] = False
            context['msg'] = u"%s" % e

        else:
            # updated values for the voted plugin
            context['plugin_rate'] = plugin.rate
            context['plugin_rate_times'] = plugin.rate_times

    context_json = simplejson.dumps(context, cls=DecimalEncoder)
    response = HttpResponse(context_json, mimetype='application/json')

    return response


class PluginDetailView(DetailView):
    """ Returns the details/info about plugin with plugin_id given
        Redirects to plugins if plugin does not exist.
    """
    model = Plugin
    context_object_name = 'plugin'
    slug_field = 'pk'
    slug_url_kwarg = 'plugin_id'

    def get(self, request, **kwargs):
        try:
            self.model.objects.get(pk=kwargs['plugin_id'])
            return super(PluginDetailView, self).get(request, **kwargs)
        except self.model.DoesNotExist:
            messages.info(request, u'The plugin you look for no longer exists '
                                   'dude. If you are a bot, please, GTFOOH.')
            return redirect(reverse('plugin_list'))


class PluginListView(ListView):
    model = Plugin


class PluginEditView(UpdateView):
    model = Plugin
    slug_name = 'plugin_id'
    form_class = PluginForm
    template_name = 'plugin-submit.html'

    def post(self, request, *args, **kwargs):
        return super(PluginEditView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        plugin = form.save()
        messages.info(self.request, u'Plugin {} updated correctly little '
                                    'dragon!'.format(plugin))
        success_url = reverse('user_detail', args=(self.request.user.username))

    def form_not_valid(self, form):
        messages.error(
            self.request,
            u'Something went wrong in your submit. Please, check it.')


# @login_required
# def plugin_edit(request, plugin_id):
#     """ Plugin edition/update view."""
#     context = {}

#     plugin = Plugin.objects.get(id=plugin_id)
#     form = PluginForm(request.POST or None,
#                       request.FILES or None,
#                       instance=plugin)

#     if request.method == 'POST':
#         if form.is_valid():
#             plugin = form.save()

#             redirect_url = reverse('user_detail', args=(request.user.username))
#             return redirect(redirect_url)
#         else:
#             messages.error(
#                 request,
#                 u'Something went wrong in your submit. Please, check it.')

#     context['form'] = form
#     return render_response(request, 'plugin-submit.html', context)
