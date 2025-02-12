from django import template
from help_functions import python_slugify

register = template.Library()


@register.filter
def slugify(s):
    return python_slugify(s)