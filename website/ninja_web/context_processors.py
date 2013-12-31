#coding=utf-8

#TODO: funtion to return (name, url) of last version
#from somewhere import latest_version
import settings


def use_lessjs(request):
    return {'use_lessjs': settings.USE_LESSJS}


def user_info(request):
    """ User machine (mac|pc|linux)
    """
    user_info = {}

    try:
        user_agent = request.META.get('HTTP_USER_AGENT', None)

        if user_agent:

            # grabbing user OS

            user_os = 'source'   # source by default
            try:
                if user_agent.index('Macintosh') > 0:
                    user_os = 'mac'
            except:
                try:
                    if user_agent.index('Linux') > 0:
                        user_os = 'linux'
                except:
                    try:
                        if user_agent.index('Windows') > 0:
                            user_os = 'win'
                    except:
                        pass

            user_info['user_os'] = user_os

            # last version available for download for this user
            #user_info['user_last_version'] = latest_version(user_os)

    except Exception, e:
        print u"Exception in context_processors.user_info: %s" % e

    return user_info
