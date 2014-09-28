from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from crispy_forms.bootstrap import StrictButton

from . import models


class ResourceForm(forms.ModelForm):

    class Meta:
        model = models.Resource
        exclude = ['created_at', 'updated_at', 'slug', 'owner']
