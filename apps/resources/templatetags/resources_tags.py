from django import template

register = template.Library()


@register.inclusion_tag('resources/includes/resource_list.html')
def resource_list(resources, profile_view=False):
    return {
        'resources': resources,
        'profile_view': profile_view
    }