# -*- coding: utf-8 *-*
import os

from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
#from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

from common import views as common_views
from ninja_profiles.forms import NinjaProfileForm
from plugins import views as plugin_views
from registration.forms import RegistrationFormUniqueEmail

admin_regex = r'^admin/'

try:
    from local_urls import admin_url
    admin_regex = r'^' + admin_url
except:
    pass


urlpatterns = patterns('',

    # Sections:
    url(r'^intro/', common_views.intro),
    url(r'^home/', common_views.intro, name="home"),
    url(r'^features/', common_views.features, name="features"),
    url(r'^using/', common_views.using, name="using"),
    url(r'^downloads/', common_views.downloads, name="downloads"),
    url(r'^contribute/', common_views.contrib, name="contribute"),
    url(r'^about/', common_views.about, name="about"),
    url(r'^updates/', common_views.updates, name="updates"),

    # Plugins:
    url(r'^plugins/', include('plugins.urls'), name="plugins"),

    # Schemes:
    url(r'^schemes/', include('schemes.urls'), name="schemes"),

    url(r'^tags/(?P<tag_id>\d+)', plugin_views.filter_by_tag,
                                  name="filter_by_tag"),
    url(r'^rate-plugin/', plugin_views.rate_plugin,
                          name="rate_plugin"),
    url(r'^people/(?P<user_name>\w+)/', common_views.user_detail,
                                        name="user_detail"),

    # Profiles:
    ('^profiles/create', 'profiles.views.create_profile',
                         {'form_class': NinjaProfileForm}),
    ('^profiles/edit', 'profiles.views.edit_profile',
                       {'form_class': NinjaProfileForm}),
    (r'^profiles/', include('profiles.urls')),

    # Homepage:
    url(r'^$', common_views.intro, name="intro"),

    # Django admin:
    url(admin_regex, include(admin.site.urls)),

    # User registration:
    (r'^accounts/register/', 'registration.views.register',
             {'form_class': RegistrationFormUniqueEmail,
              'backend': 'registration.backends.default.DefaultBackend'}),
    (r'^accounts/', include('registration.backends.default.urls')),
)

if settings.DEBUG:
    STATIC_DOC_ROOT = os.path.join(os.path.dirname(__file__), "media")

    static_pattern = patterns('django.views.static',
        url(r'^media/(?P<path>.*)$', 'serve',
                            {'document_root': STATIC_DOC_ROOT}),
        )

    urlpatterns += static_pattern
