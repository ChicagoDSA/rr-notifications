from django import template
register = template.Library()

def in_list(value,arg):
    return value in arg

def is_field(field, field_str):
    if str(field) == field_str:
        return 'foobar'
    return 'no dice'

register.filter('in_list', in_list)
register.filter('is_field', is_field)