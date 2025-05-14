from django import template
register = template.Library()
import base64

@register.filter
def encode(string):
    id = str(string)
    encoded_value=base64.b64encode(bytes(id, 'ascii'))
    return encoded_value

@register.filter
def decode(string):
    msg=base64.b64decode(string)
    decoded_value=msg.decode('ascii','strict')
    return decoded_value