from django.shortcuts import render

from . import models
from django.views.generic import ListView, DetailView


class ResourceList(ListView):
    template_name = 'resources/resource_list.html'
    queryset = models.Resource.objects.all()
    context_object_name = 'resources'


class ResourceDetail(DetailView):
    template_name = 'resources/resource_detail.html'
    model = models.Resource
    context_object_name = 'resource'
