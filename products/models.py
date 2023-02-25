from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=False, default='')

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Produkt')
    category = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='product_category', verbose_name='Kategoria')
    unit = models.CharField(max_length=4, choices=[('kg', 'kg'), ('l', 'l'), ('szt', 'szt')], default='kg',
                            verbose_name='Jednostka')
    pack_size = models.FloatField(verbose_name='Rozmiar opakowania')
    pack_price = models.FloatField(verbose_name='Cena opakowania')
    supplier = models.ForeignKey(Supplier, blank=False, related_name='product_supplier', on_delete=models.CASCADE,
                                 verbose_name='Dostawca')

    def __str__(self):
        return f'{self.name} | {self.pack_size} {self.unit} | {self.pack_price} zł | {self.supplier}'






