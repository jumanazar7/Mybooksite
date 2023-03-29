from django import template
from library.models import Author

register = template.Library()

@register.simple_tag(name="authors")
def get_all_authors():
    return Author.objects.all()