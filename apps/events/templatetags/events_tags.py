from django import template

register = template.Library()


@register.inclusion_tag('events/includes/event_list.html')
def event_list(events, profile_view=False):
    return {
        'events': events,
        'profile_view': profile_view
    }