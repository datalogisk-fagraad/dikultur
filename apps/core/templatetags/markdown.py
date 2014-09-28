import re

from django import template
from django.utils.safestring import mark_safe
import CommonMark


register = template.Library()


def convert_http_to_markdown_link(value):
    urlfinder = re.compile(r'^(http(s*):\/\/\S+)')
    urlfinder2 = re.compile(r'\s(http(s*):\/\/\S+)')
    value = urlfinder.sub(r'<\1>', value)
    return urlfinder2.sub(r' <\1>', value)


@register.filter()
def markdown(value):
    value = convert_http_to_markdown_link(value)

    parser = CommonMark.DocParser()
    renderer = CommonMark.HTMLRenderer()
    ast = parser.parse(value)
    html = renderer.render(ast)

    return mark_safe(html)
