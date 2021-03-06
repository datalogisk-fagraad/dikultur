from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, View, UpdateView, \
    CreateView
from django.core.urlresolvers import reverse

from . import models, forms
from apps.core.models import User
from ..core.views.mixins import LoginRequiredMixin

from ..events.models import Event
from ..events.utils import generate_ical


class GroupAdminRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'obj'):
            self.obj = models.Group.objects.get(slug=kwargs.get('slug'))

        if request.user not in self.obj.admins:
            return HttpResponseRedirect(self.obj.get_absolute_url())

        return super().dispatch(request, *args, **kwargs)


class GroupList(ListView):
    template_name = 'groups/group_list.html'
    context_object_name = 'groups'
    queryset = models.Group.objects.all().order_by('name')


class GroupDetail(DetailView):
    template_name = 'groups/group_detail.html'
    context_object_name = 'group'
    model = models.Group

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['future_events'] = Event.objects.filter(
            group=self.object,
            public=True,
            start__gt=timezone.now()
        )
        return context


class GroupCreate(LoginRequiredMixin, CreateView):
    template_name = 'groups/group_form.html'
    model = models.Group
    form_class = forms.GroupForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class GroupUpdate(GroupAdminRequiredMixin, UpdateView):
    template_name = 'groups/group_form.html'
    model = models.Group
    form_class = forms.GroupForm


class GroupMembers(LoginRequiredMixin, DetailView):
    template_name = 'groups/group_members.html'
    model = models.Group


class GroupJoin(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        user = self.request.user
        group = models.Group.objects.get(slug=kwargs.get('slug'))
        models.GroupMembership.objects.create(user=user, group=group)
        return HttpResponseRedirect(group.get_absolute_url())


class GroupMakeAdmin(GroupAdminRequiredMixin, View):
    def get(self, *args, **kwargs):
        user = User.objects.get(pk=kwargs.get('user_id'))
        membership = models.GroupMembership.objects.get(
            user=user, group=self.obj)
        membership.is_admin = True
        membership.save()
        return HttpResponseRedirect(
            reverse('groups:members', kwargs={'slug': self.obj.slug})
        )


class GroupRemoveAdmin(GroupAdminRequiredMixin, View):
    def get(self, *args, **kwargs):
        user = User.objects.get(pk=kwargs.get('user_id'))
        membership = models.GroupMembership.objects.get(
            user=user, group=self.obj)
        membership.is_admin = False
        membership.save()
        return HttpResponseRedirect(
            reverse('groups:members', kwargs={'slug': self.obj.slug})
        )


class GroupICal(View):
    def get(self, *args, **kwargs):
        cal = generate_ical(group__slug=kwargs.get('slug'))
        return HttpResponse(content=cal.to_ical())
