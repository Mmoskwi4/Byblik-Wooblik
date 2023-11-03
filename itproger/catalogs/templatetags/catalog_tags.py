from django import template
from catalogs.models import *

register = template.Library()

@register.inclusion_tag('catalogs/catalog_category.html')
def draw_category(cat_selected=0):
    category = Category.objects.all()
    return {'category': category, 'cat_selected': cat_selected}

@register.inclusion_tag('catalogs/catalog_cake.html')
def draw_cake(cat_selected=0):
    cakes = Cake.objects.all()
    return {'cakes': cakes, 'cat_selected': cat_selected}