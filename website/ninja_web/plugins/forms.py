# encoding: utf-8
from django import forms

from plugins.models import Plugin


class PluginForm(forms.ModelForm):

    class Meta:
        model = Plugin
        exclude = ['user', 'upload_date']

#    def __init__(self, *args, **kwargs):
#        self.fields['user'] = kwargs.pop('user', None)
#        super(PluginForm, self).__init__(*args, **kwargs)
