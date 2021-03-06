from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from ..core.views.mixins import LoginRequiredMixin

from . import models, forms


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


@login_required
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


@login_required
@csrf_exempt
def resource_remove_upvote(request, **kwargs):
    slug = kwargs.get('slug', None)
    resource = models.Resource.objects.get(slug=slug)
    resource.remove_upvote(request.user)
    return HttpResponse(content=resource.upvotes, status=200)


class ResourceCreate(LoginRequiredMixin, CreateView):
    template_name = 'resources/resource_form.html'
    model = models.Resource
    form_class = forms.ResourceForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        resource = form.save()

        for file in self.request.FILES.getlist('resourcefile'):
            models.ResourceFile.objects.create(resource=resource, file=file)

        return HttpResponseRedirect(resource.get_absolute_url())


class ResourceUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'resources/resource_form.html'
    model = models.Resource
    form_class = forms.ResourceForm

    def form_valid(self, form):
        resource = form.save()
        for file in self.request.FILES.getlist('resourcefile'):
            models.ResourceFile.objects.create(resource=resource, file=file)

        return HttpResponseRedirect(resource.get_absolute_url())


@login_required
@csrf_exempt
def resource_file_delete(request, **kwargs):
    pk = request.POST.get('pk', None)

    if pk:
        file = models.ResourceFile.objects.get(pk=pk)
        file.delete()
        return HttpResponse(status=200)

    # Something went wrong
    return HttpResponse(status=500)
