from django.conf import settings


def globals(request):
    """ Global variables of Ninja website
    """

    globals_dict = {
        'LESS_DEBUG': settings.LESS_DEBUG
    }
    return globals_dict
