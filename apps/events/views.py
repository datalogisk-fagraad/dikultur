from django.views.generic import ListView, DetailView, CreateView, UpdateView

from . import models, forms


class EventList(ListView):
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    queryset = models.Event.objects.filter(public=True)


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
