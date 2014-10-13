from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from crispy_forms.bootstrap import StrictButton

from . import models


class GroupForm(forms.ModelForm):

    class Meta:
        model = models.Group
        exclude = ['created_at', 'updated_at', 'slug', 'members']

    def __init__(self, *args, user=None, **kwargs):
        self.user = user

        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.form_method = 'POST'

        field_list = [
            'name', 'description', 'website', 'email', 'mailinglist_signup',
            Div(
                StrictButton('Save', type='submit', css_class='btn-primary'),
                css_class="text-right"
            )
        ]

        self.helper.layout = Layout(
            *field_list
        )

    def save(self, commit=True):
        created = True if self.instance.pk is None else False

        instance = super().save(commit)

        if created:
            models.GroupMembership.objects.create(
                group=instance,
                user=self.user,
                is_admin=True,
            )

        return instance
