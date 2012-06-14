# -*- coding: utf-8 *-*
from django.http import HttpResponse

from schemes.models import Scheme

try:
    import json
except ImportError:
    import simplejson as json


def get_schemes_dict(request):
    """ Returns the list of all schemes with metadata.
    """

    schemes = []  # dict to return
    schemes_list = Scheme.objects.all()  # initial query

    for scheme in schemes_list:
        scheme_data = {}
        scheme_data['name'] = scheme.name
        scheme_data['download'] = scheme.get_download_url
        scheme_data['preview'] = scheme.get_absolute_url
        scheme_data['authors'] = scheme.user.get_full_name()

        schemes.append(scheme_data)

    return HttpResponse(json.dumps(schemes), mimetype="application/json")
