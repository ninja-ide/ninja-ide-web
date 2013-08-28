# -*- coding: utf-8 *-*
import os

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import ListView, TemplateView

from django.contrib import admin
admin.autodiscover()

from articles.models import Article
from registration.forms import RegistrationFormUniqueEmail

from common.views import UserDetailView
from plugins import views as plugin_views

admin_regex = r'^admin/'

try:
    from local_urls import admin_url
    admin_regex = r'^' + admin_url
except:
    pass


urlpatterns = patterns(
    '',

    # Homepage:
    url(r'^intro/', TemplateView.as_view(
        template_name="intro.html"),
        name="intro_home"),

    url(r'^home/', TemplateView.as_view(
        template_name="intro.html"),
        name="home"),

    url(r'^features/', TemplateView.as_view(
        template_name="features.html"),
        name="features"),

    url(r'^using/', TemplateView.as_view(
        template_name="using.html"),
        name="using"),

    url(r'^downloads/', TemplateView.as_view(
        template_name="downloads.html"),
        name="downloads"),

    url(r'^contribute/', TemplateView.as_view(
        template_name="contrib.html"),
        name="contribute"),

    url(r'^wisdom/$', ListView.as_view(
        model=Article,
        template_name='blog/post_list.html'),
        name="ninja_wisdom"),

    url(r'^wisdom/', include('articles.urls')),

    url(r'^about/', TemplateView.as_view(
        template_name="about.html"),
        name="about"),

    url(r'^updates/', TemplateView.as_view(
        template_name="updates_simple.html"),
        name="updates"),


    # Ninja stuff:
    url(r'^plugins/', include('plugins.urls'), name="plugins"),
    url(r'^schemes/', include('schemes.urls'), name="schemes"),

    url(r'^tags/(?P<tag_id>\d+)',
        plugin_views.filter_by_tag,
        name="filter_by_tag"),

    url(r'^rate-plugin/',
        plugin_views.rate_plugin,
        name="rate_plugin"),

    url(r'^people/(?P<user_name>\w+)/',
        UserDetailView.as_view(),
        name="user_detail"),

    # Profiles:
    # ('^profiles/create', 'profiles.views.create_profile',
    #                      {'form_class': NinjaProfileForm}),
    # ('^profiles/edit', 'profiles.views.edit_profile',
    #                    {'form_class': NinjaProfileForm}),
    #(r'^profiles/', include('profiles.urls')),


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

    static_pattern = patterns(
        'django.views.static',

        url(r'^media/(?P<path>.*)$', 'serve',
            {'document_root': STATIC_DOC_ROOT}),
    )

    urlpatterns += static_pattern
