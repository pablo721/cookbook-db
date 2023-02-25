from django.contrib import admin
from .models import Product, ProductCategory, Supplier
# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Supplier)
admin.site.register(Product)



