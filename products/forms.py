from django import forms
from .models import ProductCategory, Supplier

class NewSupplier(forms.Form):
    name = forms.CharField(label='Nazwa firmy', max_length=32)


class NewProduct(forms.Form):
    name = forms.CharField(label='Nazwa', max_length=32)
    category = forms.ChoiceField(label='Kategoria')
    unit = forms.ChoiceField(label='Jednostka', choices=[('kg', 'kg'), ('l', 'l'), ('szt', 'szt')])
    pack_size = forms.FloatField(label='Wielkość opakowania')
    pack_price = forms.FloatField(label='Cena opakowania (zł)')
    supplier = forms.ChoiceField(label='Dostawca')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = [(c.id, c.name) for c in ProductCategory.objects.all()]
        self.fields['supplier'].choices = [(c.id, c.name) for c in Supplier.objects.all()]



