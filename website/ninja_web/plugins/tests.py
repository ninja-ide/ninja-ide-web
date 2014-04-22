"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.urlresolvers import reverse


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class PluginBaseTest(TestCase):
    def setup(self):
        pass


class PluginListTest(PluginBaseTest):
    def test_list_returns_page_ok(self):
        list_url = reverse('plugin_list')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, 200)
