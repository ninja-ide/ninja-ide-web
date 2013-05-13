# -*- coding: utf-8 *-*
from django.conf.urls.defaults import *
from blog.feeds import LatestPostsFeed


urlpatterns = patterns('basic.blog.views',
    url(r'feed/?$',
        LatestPostsFeed()),

    url(r'(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        'post_detail',
        {'extra_context': {'on_news': 'true'}},
        name='blog_detail'),

    url(r'(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/$',
        'post_archive_day',
        {'extra_context': {'on_news': 'true'}},
        name='blog_archive_day'),

    url(r'(?P<year>\d{4})/(?P<month>\w{3})/$',
        'post_archive_month',
        {'extra_context': {'on_news': 'true'}},
        name='blog_archive_month'),

    url(r'(?P<year>\d{4})/$',
        'post_archive_year',
        {'extra_context': {'on_news': 'true'}},
        name='blog_archive_year'),

    # url(r'^news/categories/(?P<slug>[-\w]+)/$',
    #     'category_detail',
    #     {'extra_context' : {'on_news': 'true',},},
    #     name='blog_category_detail'
    # ),
    # url (r'^news/categories/$',
    #     view='category_list',
    #     name='blog_category_list'
    # ),

    url(r'tags/(?P<slug>[-\w]+)/$',
        'tag_detail',
        {'extra_context': {'on_news': 'true'}},
        name='blog_tag_detail'),

    url(r'search/$',
        'search',
        {'extra_context': {'on_news': 'true'}},
        name='blog_search'),

    url(r'page/(?P<page>\w)/$',
        'post_list',
        {'extra_context': {'on_news': 'true'}},
        name='blog_index_paginated'),

    url(r'$',
        'post_list',
        {'extra_context': {'on_news': 'true'}},
        name='blog_index'),
)
