from django.views.generic import ListView, DetailView, CreateView, UpdateView

from . import models, forms


class EventList(ListView):
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    queryset = models.Event.objects.all()


class EventDetail(DetailView):
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
    model = models.Event


class EventCreate(CreateView):
    template_name = 'events/event_form.html'
    model = models.Event
    form_class = forms.EventForm


class EventUpdate(UpdateView):
    template_name = 'events/event_form.html'
    model = models.Event
    form_class = forms.EventForm