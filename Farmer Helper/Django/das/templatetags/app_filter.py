from django import template
register=template.Library()

@register.filter(name="remove_trash")
def remove_trash(value):
    value_str=str(value)
    value_splice=value_str[27:-2]
    value_splice=value_splice.replace(" ","")
    return value_splice