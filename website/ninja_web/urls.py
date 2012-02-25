# -*- coding: utf-8 *-*
import os

from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
#from django.views.generic.base import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from registration.forms import RegistrationFormUniqueEmail

from common import views
from plugins import views as plugin_views

admin_regex = r'^admin/'
try:
    from local_urls import admin_url
    admin_regex = r'^' + admin_url
except:
    pass


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ninja_web.views.home', name='home'),
    # url(r'^ninja_web/', include('ninja_web.foo.urls')),

    url(r'^intro/', views.intro),
    url(r'^features/', views.features),
    url(r'^using/', views.using),
    url(r'^downloads/', views.downloads),
    url(r'^contrib/', views.contrib),
    url(r'^about/', views.about),

    url(r'^updates/', views.updates),
    url(r'^community/', views.community),

    url(r'^plugins/schemes', views.schemes),
    url(r'^plugins/oficial', views.oficial),    # to be deprecated
    url(r'^plugins/official', views.official),
    url(r'^plugins/community', views.community),
    url(r'^plugins/submit/$', plugin_views.plugin_submit, name="plugin_submit"),
    url(r'^plugins/(?P<plugin_id>\d+)/$', plugin_views.plugin, name="plugin_detail"),
    url(r'^plugins/$', plugin_views.plugins, name="plugins"),

    url(r'^tags/(?P<tag_id>\d+)', plugin_views.filter_by_tag, name="filter_by_tag"),

    #url(r'^vote-plugin/(?P<plugin_id>\d+)/(?P<rate>\d+{1-5})',
    url(r'^rate-plugin/', plugin_views.rate_plugin, name="rate_plugin"),

    url(r'^people/(?P<user_name>\w+)/', views.user_detail, name="user_detail"),

    url(r'^$', views.intro),

    # Uncomment the admin/doc line below to enable admin documentation:
#    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(admin_regex, include(admin.site.urls)),
    #(r'^admin/', include(admin.site.urls)),

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
