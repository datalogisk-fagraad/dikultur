from django.db import IntegrityError
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from . import models


class ResourceList(ListView):
    template_name = 'resources/resource_list.html'
    queryset = models.Resource.objects.all()
    context_object_name = 'resources'


class ResourceDetail(DetailView):
    template_name = 'resources/resource_detail.html'
    model = models.Resource
    context_object_name = 'resource'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Anonymous users can't like stuff
        if not user.is_anonymous():
            try:
                context['has_liked'] = models.ResourceUpvote.objects.filter(
                    user=user,
                    resource=self.object
                ).exists()
            except models.ResourceUpvote.DoesNotExist:
                context['has_liked'] = False
        return context


@csrf_exempt
def resource_upvote(request, **kwargs):
    slug = kwargs.get('slug', None)
    resource = models.Resource.objects.get(slug=slug)

    # Handle if the resource already is upvoted by the user
    # Should not happen, but everything is possible...
    try:
        resource.upvote(request.user)
    except IntegrityError:
        return HttpResponse(status=500)

    return HttpResponse(content=resource.upvotes, status=200)


@csrf_exempt
def resource_remove_upvote(request, **kwargs):
    slug = kwargs.get('slug', None)
    resource = models.Resource.objects.get(slug=slug)
    resource.remove_upvote(request.user)
    return HttpResponse(content=resource.upvotes, status=200)
