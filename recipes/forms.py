from django import forms
from .models import RecipeCategory
from products.models import Product


class NewRecipe(forms.Form):
    name = forms.CharField(label='Nazwa', max_length=32)
    category = forms.ChoiceField(label='Kategoria')
    price = forms.FloatField(label='Cena')
    author = forms.CharField(label='Autor', max_length=32)
    grammage = forms.IntegerField(label='Gramatura')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = [(c.id, c.name) for c in RecipeCategory.objects.all()]


class EditRecipe(forms.Form):
    name = forms.CharField(label='Nazwa', max_length=32, required=False)
    price = forms.FloatField(label='Cena', required=False)
    author = forms.CharField(label='Autor', max_length=32, required=False)
    grammage = forms.IntegerField(label='Gramatura', required=False)


class AddToRecipe(forms.Form):
    product = forms.ChoiceField(label='Produkt')
    amount = forms.FloatField(label='Ilość (szt/g/ml)', max_value=100000)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].choices = [(c.id, c.name) for c in Product.objects.all()]











