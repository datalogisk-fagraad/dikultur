from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from crispy_forms.bootstrap import StrictButton

from . import models


class EventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = ('title', 'place', 'datetime', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            'title', 'place', 'datetime', 'description',
            Div(
                StrictButton('Create', type='submit', css_class='btn-primary'),
                css_class="text-right"
            )
        )

