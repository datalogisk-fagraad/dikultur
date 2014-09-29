import icalendar

from . import models


def generate_ical(**filters):
    cal = icalendar.Calendar()
    for event in models.Event.objects.filter(**filters):
        if event.ical and event.public:
            event_ical = icalendar.Event.from_ical(event.ical)
            cal.add_component(event_ical)

    return cal
