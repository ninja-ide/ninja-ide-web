# encoding: utf-8
from django import forms

from schemes.models import Scheme


class SchemeForm(forms.ModelForm):

    class Meta:
        model = Scheme
        exclude = ['user', 'upload_date']
