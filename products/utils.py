import yaml
from .models import ProductCategory


PRODUCT_CATEGORIES = ['Ryby', 'Owoce morza', 'Warzywa', 'Owoce', 'Produkty suche', 'Mięso', 'Napoje']


def setup_product_categories():
    for category in PRODUCT_CATEGORIES:
        obj = ProductCategory.objects.create(name=category)
        obj.save()