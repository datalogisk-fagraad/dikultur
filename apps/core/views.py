from django.shortcuts import render

from django.views.generic import TemplateView


class FrontPage(TemplateView):
    template_name = 'core/frontpage.html'
