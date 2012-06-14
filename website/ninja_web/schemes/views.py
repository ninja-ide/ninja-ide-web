# encoding: utf-8
from decimal import Decimal

from tagging.models import Tag

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils import simplejson

from common.utils import render_response
from schemes.forms import SchemeForm
from schemes.models import Scheme

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
    Given a tag id, return all schemes with this tag.
    """
    tag = None
    context = {}

    try:
        tag = Tag.objects.get(id=tag_id)
        context['schemes_tag'] = tag.name
    except:
        pass
    else:
        context['schemes'] = Scheme.objects.filter(tags__icontains=tag.name)

    return render_response(request, 'schemes.html', context)


@login_required
def scheme_submit(request):
    context = {}

    form = SchemeForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            new_scheme = form.save(commit=False)
            new_scheme.user = request.user
            new_scheme.save()
            messages.info(request, u'Scheme submitted correctly little dragon.')

            return redirect('schemes')
        else:
            messages.error(
                    request,
                    u'Something went wrong in your submit. Please, check it.')

    context['form'] = form
    return render_response(request, 'scheme-submit.html', context)


def get_scheme(request, scheme_id=None):
    context = {}

    try:
        context['scheme'] = Scheme.objects.get(pk=scheme_id)
    except Scheme.DoesNotExist:
        pass

    return render_response(request, 'scheme-detail.html', context)


def schemes(request):
    context = {}
    context['schemes'] = Scheme.objects.all()
    return render_response(request, 'schemes.html', context)


@login_required
def scheme_edit(request, scheme_id):
    """ scheme edition/update view."""
    context = {}

    scheme = Scheme.objects.get(id=scheme_id)
    form = SchemeForm(request.POST or None,
                      request.FILES or None,
                      instance=scheme)

    if request.method == 'POST':
        if form.is_valid():
            messages.info(request, u'scheme updated correctly little dragon!')

            redirect_url = reverse('user_detail', args=(request.user.username,))
            return redirect(redirect_url)
        else:
            messages.error(
                    request,
                    u'Something went wrong in your submit. Please, check it.')

    context['form'] = form
    return render_response(request, 'scheme-submit.html', context)
