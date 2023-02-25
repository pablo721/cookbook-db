from django.contrib import admin
from .models import Recipe, Amount, RecipeCategory
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Amount)
admin.site.register(RecipeCategory)


