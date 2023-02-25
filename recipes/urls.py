
from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('<category>', views.recipes_cat, name='recipes_cat'),
    path('<category>/<recipe_name>', views.recipes_recipe, name='recipes_recipe'),
]


