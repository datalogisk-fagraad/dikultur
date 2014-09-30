from django.shortcuts import render

from django.views.generic import TemplateView

from allauth.account.views import LogoutView


class FrontPage(TemplateView):
    template_name = 'core/frontpage.html'


class ProfileView(TemplateView):
    template_name = 'core/profile.html'


class Logout(LogoutView):
    template_name = 'core/logout.html'
