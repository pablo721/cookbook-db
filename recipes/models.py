from django.db import models
from products.models import Product


class RecipeCategory(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=False, default='')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=32, unique=True)
    category = models.ForeignKey(RecipeCategory, on_delete=models.CASCADE, related_name='recipe_category',
                                 blank=False, default=1)
    products = models.ManyToManyField(Product, blank=True, related_name='recipe_products', through='amount',
                                      through_fields=('recipe', 'product'))
    price = models.FloatField(unique=False, blank=True, default=0)
    author = models.CharField(max_length=64, unique=False, blank=True, default='Filip Herba')
    grammage = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Amount(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_amount')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_amount')
    amount = models.FloatField()












