# encoding: utf-8
from django import forms

from plugins.models import Plugin


class PluginForm(forms.ModelForm):

    class Meta:
        model = Plugin
        exclude = ['user', 'upload_date']
        required_css_class = 'required'
        error_css_class = 'error'
