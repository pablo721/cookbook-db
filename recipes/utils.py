from .models import RecipeCategory
import os
import yaml



RECIPE_CATEGORIES = ['Zupy', 'Przystawki', 'Dania główne', 'Tatary', 'Sashimi', 'Gunkany', 'Hosomaki', 'Nigiri',
                     'Futomaki', 'California', 'Zestawy', 'Dodatki', 'Napoje']




def setup_recipe_categories():
    for category in RECIPE_CATEGORIES:
        obj = RecipeCategory.objects.create(name=category)
        obj.save()


def recipe_data(ingredients):
    table_data = []
    total_cost = 0
    for item in ingredients:
        product = item.product
        unit_price = (float(product.pack_price) / float(product.pack_size)).__round__(2)
        product_cost = (unit_price * (item.amount / 1000)).__round__(2)
        table_data.append([product.name, product.unit, unit_price, item.amount, product_cost])
        total_cost += product_cost

    return {'table_data': table_data, 'total_cost': total_cost}











