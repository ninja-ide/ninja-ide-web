from datetime import datetime

from django.template import Library, Node, TemplateSyntaxError  # , resolve_variable

from plugins.models import Plugin

register = Library()


class LastPluginsNode(Node):
    def __init__(self, max_plugins=5, var_name='last_plugins'):
        self.max = int(max_plugins)
        self.var_name = var_name

    def render(self, context):
        plugins = Plugin.objects.filter(upload_date__lte=datetime.now).order_by('-upload_date')[:self.max]

        if self.var_name:
            context[self.var_name] = plugins
        else:
            return plugins

        return ''


def last_plugins(parser, token):
    """ Get the latest plugins (by upload date) and returns them
        --------
        usage:

        {% last_plugins 4 %}
        will create/load the context variable 'last_plugins' with
        the last 4 plugins uploaded.

        {% last_plugins 4 as poopi %}
        same as before but the variable is 'poopi'
    """
    def syntax_error():
        raise TemplateSyntaxError("example: last_plugins <value> [as <context_variable>]")
    args = token.contents.split()
    if len(args) == 4:
        if args[2] != 'as':
            syntax_error()
        ret = LastPluginsNode(args[1], args[3])
    elif len(args) == 2:
        ret = LastPluginsNode(args[1])
    else:
        syntax_error()
    return ret

register.tag("last_plugins", last_plugins)
