from django import template

register = template.Library()

@register.filter(name='priority_color')
def priority_color(value):
    if value == 1:
        return "success"
    elif value == 2:
        return "warning"
    elif value == 3:
        return "danger"
    return "secondary"