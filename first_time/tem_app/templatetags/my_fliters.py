from django import template

register = template.Library()


@register.filter(is_safe=False)
def upper_number(value):
    return 0
