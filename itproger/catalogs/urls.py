from django.urls import path
from .views import *

urlpatterns = [
    path('classiccake/', catalog, name='catalog'),
    path('<slug:cat_slug>/', show_category, name='category'),
    path('<slug:cat_slug>/<int:cake_id>/', show_cake, name='cake'),
]
