from django.shortcuts import render

from django.views.generic import TemplateView


class FrontPage(TemplateView):
    template_name = 'core/frontpage.html'


class ProfileView(TemplateView):
    template_name = 'core/profile.html'
