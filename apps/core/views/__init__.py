from django.shortcuts import render

from django.views.generic import TemplateView

from allauth.account.views import LogoutView

from ...events.models import Event


class FrontPage(TemplateView):
    template_name = 'core/frontpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.filter(
            public=True).order_by('datetime')[:5]
        return context


class ProfileView(TemplateView):
    template_name = 'core/profile.html'


class Logout(LogoutView):
    template_name = 'core/logout.html'
