# encoding: utf-8
from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import simplejson

from common.utils import render_response
from plugins.forms import PluginForm
from plugins.models import Vote, Plugin


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


@login_required
def plugin_submit(request):
    dict = {}

    if request.method == 'POST':
        form = PluginForm(request.POST, request.FILES)

        if form.is_valid():

            lala = form.save()
            lala.user = request.user
            lala.save()
#            import pdb; pdb.set_trace()
            messages.info(request, u'Plugin submitted correctly little dragon.')

            return redirect('plugins')
        else:
            messages.error(
                    request,
                    u'Something went wrong in your submit. Please, check it.')
    else:
        form = PluginForm()

    dict['form'] = form

    return render_response(request, 'plugin-submit.html', dict)


@login_required
def rate_plugin(request):

    data = {}
    print 'Carnevali'
    if request.method == 'GET':
        plugin_id = request.GET.get('plugin_id', False)
        rate = request.GET.get('rate', 0)

    if plugin_id and rate > 0:
        new_vote = Vote(plugin_id=int(plugin_id),
                        user=request.user,
                        rate=int(rate),
                        voter_ip=request.META['REMOTE_ADDR'],
                        )

        try:
            # este save tira un error por el unique together. Hay que cargar un
            # mensajito de error (el de ya votaste este plugin).
            new_vote.save()
        except Exception, e:
#            import pdb; pdb.set_trace()
            data['ok'] = False
            data['error'] = u'%s' % e

    else:

        data['plugin_rate'] = new_vote.rate
        data['plugin_rate_times'] = new_vote.rate_times

        data = simplejson.dumps(data, cls=DecimalEncoder)
        response = HttpResponse(data, mimetype='application/json')

    return response


def plugin(request, plugin_id=None):
    dict = {}

    if plugin_id:
        try:
            dict['plugin'] = Plugin.objects.get(pk=plugin_id)
        except:
            pass

    # some another extra info for this plugin:
    # dict['extra'] = blabla
    # ...

    return render_response(request, 'plugin-detail.html', dict)


def plugins(request):
    dict = {}

    """
    if some-category-selected:
        dict['plugin-category'] = the-category
    """
    dict['plugins'] = Plugin.objects.all()
    return render_response(request, 'plugins.html', dict)
