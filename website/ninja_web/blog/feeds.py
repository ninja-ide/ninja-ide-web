#!/usr/bin/env python
# coding: utf-8

"""
Feeds for the blog application.
"""

from django.contrib.syndication.views import Feed
from basic.blog.models import Post


class LatestPostsFeed(Feed):
    title = "Machinalis blog posts"
    link = "/blog/"
    description = "Blog posts of machinalis."

    def items(self):
        return Post.objects.published().order_by("-publish")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_pubdate(self, item):
        return item.publish

    def item_author_name(self, item):
        return item.author
