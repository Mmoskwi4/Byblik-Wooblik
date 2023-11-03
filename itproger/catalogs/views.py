from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def catalog(request, cat_selected=1):
    return render(request, 'catalogs/catalog.html', {'cat_selected': cat_selected})

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    cakes = Cake.objects.all()

    context = {
        'category': category,
        'cakes': cakes,
        'cat_selected': category.pk,
        'cat_selected_active': category.name
    }
    return render(request, 'catalogs/catalog.html', context)

def show_cake(request, cat_slug, cake_id):
    category = get_object_or_404(Category, slug=cat_slug)
    cakes = get_object_or_404(Cake, pk=cake_id)

    context = {
        'category': category,
        'cakes': cakes,
        'cat_selected': cakes.cat_id
    }

    return render(request, 'catalogs/card_cake.html', context)