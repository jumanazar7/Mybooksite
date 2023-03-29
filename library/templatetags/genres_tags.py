from django import template
from library.models import Genre

register = template.Library()

@register.simple_tag(name="genres")
def get_all_genres():
    return Genre.objects.all()