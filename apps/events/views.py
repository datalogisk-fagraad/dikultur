from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    View

from django.utils import timezone

import icalendar

from . import models, forms


class EventList(ListView):
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    queryset = models.Event.objects.filter(
        public=True, datetime__gt=timezone.now()).order_by('datetime')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['past_events'] = models.Event.objects.filter(
            public=True, datetime__lt=timezone.now()).order_by('datetime')
        return context


class EventDetail(DetailView):
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
    model = models.Event


class EventCreate(CreateView):
    template_name = 'events/event_form.html'
    model = models.Event
    form_class = forms.EventForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EventUpdate(UpdateView):
    template_name = 'events/event_form.html'
    model = models.Event
    form_class = forms.EventForm


class CalendarFeed(View):
    def get(self, *args):
        cal = icalendar.Calendar()
        for event in models.Event.objects.all():
            if event.ical and event.public:
                event_ical = icalendar.Event.from_ical(event.ical)
                cal.add_component(event_ical)

        return HttpResponse(content=cal.to_ical())
