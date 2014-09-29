from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import ListView, DetailView, View

from . import models

from ..events.models import Event
from ..events.utils import generate_ical


class GroupList(ListView):
    template_name = 'groups/group_list.html'
    context_object_name = 'groups'
    queryset = models.Group.objects.all()


class GroupDetail(DetailView):
    template_name = 'groups/group_detail.html'
    context_object_name = 'group'
    model = models.Group

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['future_events'] = Event.objects.filter(
            group=self.object,
            public=True,
            datetime__gt=timezone.now()
        )
        return context


class GroupICal(View):
    def get(self, *args, **kwargs):
        cal = generate_ical(group__slug=kwargs.get('slug'))
        return HttpResponse(content=cal.to_ical())
