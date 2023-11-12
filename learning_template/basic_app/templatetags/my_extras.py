from django import template

register = template.Library()

# or use decorator
@register.filter(name='cut')

def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# string passed to register.filter is the name of the function
# register.filter('cut',cut)

