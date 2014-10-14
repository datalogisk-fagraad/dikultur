from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from crispy_forms.bootstrap import StrictButton

from . import models


class EventForm(forms.ModelForm):

    class Meta:
        model = models.Event
        exclude = ['created_at', 'updated_at', 'slug', 'owner']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.form_method = 'POST'

        field_list = [
            'title', 'place', 'start', 'end', 'description', 'tags',
        ]

        if user:
            if len(user.group_set.all()) > 0:
                self.fields['group'] = forms.ModelChoiceField(
                    queryset=user.group_set.all(),
                    required=False,
                )
                field_list.append('group')

        field_list.append('public')

        field_list.append(
            Div(
                StrictButton('Save', type='submit', css_class='btn-primary'),
                css_class="text-right"
            )
        )

        self.helper.layout = Layout(
            *field_list
        )

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start')
        end = cleaned_data.get('end')

        if end and end < start:
            self.add_error('start', 'Start cannot be after end.')
            self.add_error('end', 'End cannot be before start.')
