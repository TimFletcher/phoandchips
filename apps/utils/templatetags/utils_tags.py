from django import template

register = template.Library()

@register.simple_tag
def active(request, pattern):
    import re
    if re.search(pattern, request.path):
        return "id='current'"
    return ''

@register.simple_tag
def random_number():
    import random
    return "%03d" % random.randint(1,5)