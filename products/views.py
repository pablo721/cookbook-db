from django.shortcuts import render
from .models import Product, ProductCategory, Supplier
from django.contrib.auth.decorators import login_required
from .utils import setup_product_categories
from .forms import NewProduct, NewSupplier
# Create your views here.


@login_required
def products(request):
    context = dict()
    context['products'] = Product.objects.all()
    context['suppliers'] = Supplier.objects.all()
    categories = ProductCategory.objects.all()
    context['categories'] = categories
    context['fields'] = ['Produkt', 'Wielkość opakowania', 'Cena opakowania', 'Cena jednostkowa', 'Dostawca']

    if not len(categories):
        setup_product_categories()

    if request.method == 'POST' and 'unit' in str(request.POST):
        form_new_product = NewProduct(request.POST)
        if form_new_product.is_valid():
            form_data = form_new_product.cleaned_data
            new_product = Product.objects.create(name=form_data['name'],
                                                 category=ProductCategory.objects.get(id=form_data['category']),
                                                 unit=form_data['unit'], pack_size=form_data['pack_size'],
                                                 pack_price=form_data['pack_price'],
                                                 supplier=Supplier.objects.get(id=form_data['supplier']))
            new_product.save()
        else:
            print(form_new_product.errors)

    elif request.method == 'POST' and 'name' in str(request.POST):
        form_new_supplier = NewSupplier(request.POST)
        if form_new_supplier.is_valid():
            form_data = form_new_supplier.cleaned_data
            new_supplier = Supplier.objects.create(**form_data)
            new_supplier.save()
            print('saved supp')

    elif request.method == 'POST' and request.is_ajax:
        ids = request.POST['checked_ids'].split(',')
        for prod_id in ids:
            Product.objects.get(id=int(prod_id)).delete()

    context['form_new_product'] = NewProduct()
    context['form_new_supplier'] = NewSupplier()
    return render(request, 'products/products.html', context=context)


@login_required
def products_category(request, category):
    context = dict()
    context['products'] = Product.objects.filter(category=ProductCategory.objects.get(name=category))
    context['suppliers'] = Supplier.objects.all()
    categories = ProductCategory.objects.all()
    context['categories'] = categories
    context['fields'] = ['Produkt', 'Wielkość opakowania', 'Cena opakowania', 'Cena jednostkowa', 'Dostawca']

    if not len(categories):
        setup_product_categories()

    if request.method == 'POST' and 'unit' in str(request.POST):
        form_new_product = NewProduct(request.POST)
        if form_new_product.is_valid():
            form_data = form_new_product.cleaned_data
            new_product = Product.objects.create(name=form_data['name'],
                                                 category=ProductCategory.objects.get(id=form_data['category']),
                                                 unit=form_data['unit'], pack_size=form_data['pack_size'],
                                                 pack_price=form_data['pack_price'],
                                                 supplier=Supplier.objects.get(id=form_data['supplier']))
            new_product.save()
        else:
            print(form_new_product.errors)

    elif request.method == 'POST' and 'name' in str(request.POST):
        form_new_supplier = NewSupplier(request.POST)
        if form_new_supplier.is_valid():
            form_data = form_new_supplier.cleaned_data
            new_supplier = Supplier.objects.create(**form_data)
            new_supplier.save()

    elif request.method == 'POST' and request.is_ajax:
        ids = request.POST['checked_ids'].split(',')
        for prod_id in ids:
            Product.objects.get(id=int(prod_id)).delete()

    context['form_new_product'] = NewProduct()
    context['form_new_supplier'] = NewSupplier()

    return render(request, 'products/products.html', context)


