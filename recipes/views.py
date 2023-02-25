from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import NewRecipe, EditRecipe, AddToRecipe
from .models import Product, Recipe, Amount, RecipeCategory
from .utils import recipe_data, setup_recipe_categories
from django.contrib.auth.decorators import login_required



@login_required
def recipes(request):
    context = dict()
    context['recipes'] = Recipe.objects.all()
    context['category'] = 0
    context['categories'] = RecipeCategory.objects.all()

    if not len(context['categories']):
        setup_recipe_categories()

    if request.method == 'POST' and 'price' in str(request.POST):
        form_new_recipe = NewRecipe(request.POST)
        if form_new_recipe.is_valid():
            form_data = form_new_recipe.cleaned_data
            new_recipe = Recipe.objects.create(name=form_data['name'],
                                               category=RecipeCategory.objects.get(id=form_data['category']),
                                               price=form_data['price'],
                                               author=form_data['author'],
                                               grammage=form_data['grammage'])
            new_recipe.save()
            return HttpResponseRedirect(reverse('recipes:recipes_cat', args=(new_recipe.category,)))
        else:
            print(form_new_recipe.errors)

    else:
        context['form_new_recipe'] = NewRecipe()
        print(context)
        return render(request, 'recipes/recipes.html', context=context)


@login_required
def recipes_cat(request, category):
    context = {}
    category_obj = RecipeCategory.objects.get(name=category)
    context['recipes'] = Recipe.objects.filter(category=category_obj)
    context['categories'] = RecipeCategory.objects.all()
    context['category'] = category_obj

    if request.method == 'POST' and 'price' in str(request.POST):
        form_new_recipe = NewRecipe(request.POST)
        if form_new_recipe.is_valid():
            form_data = form_new_recipe.cleaned_data
            new_recipe = Recipe.objects.create(name=form_data['name'],
                                               category=RecipeCategory.objects.get(id=form_data['category']),
                                               price=form_data['price'],
                                               author=form_data['author'],
                                               grammage=form_data['grammage'])
            new_recipe.save()
            return HttpResponseRedirect(reverse('recipes:recipes_cat', args=(category,)))
        else:
            print(form_new_recipe.errors)

    context['form_new_recipe'] = NewRecipe()
    return render(request, 'recipes/recipes.html', context=context)


@login_required
def recipes_recipe(request, category, recipe_name):
    context = dict()
    recipe = Recipe.objects.get(name=recipe_name)
    recipes = Recipe.objects.filter(category=recipe.category)
    context['recipe'] = recipe.name
    context['recipes'] = recipes
    context['category'] = recipe.category
    context['categories'] = RecipeCategory.objects.all()

    if request.method == 'POST' and 'amount' in str(request.POST):
        form_add_to_recipe = AddToRecipe(request.POST)
        if form_add_to_recipe.is_valid():
            form_data = form_add_to_recipe.cleaned_data
            product = Product.objects.get(id=form_data['product'])

            if Amount.objects.filter(recipe=recipe).filter(product=product).exists():
                new_amount = Amount.objects.filter(recipe=recipe).filter(product=product)
                amount = Amount.objects.get(id=new_amount[0].id)
                amount.amount = form_data['amount']
                amount.save()
                return HttpResponseRedirect(reverse('recipes:recipes_recipe', args=(category, recipe)))
            else:
                new_ingredient = Amount.objects.create(recipe=recipe, product=product, amount=form_data['amount'])
                new_ingredient.save()
                return HttpResponseRedirect(reverse('recipes:recipes_recipe', args=(category, recipe)))

    elif request.method == 'POST' and 'grammage' in str(request.POST):
        form_edit_recipe = EditRecipe(request.POST)
        if form_edit_recipe.is_valid():
            form_data = form_edit_recipe.cleaned_data
            for k, v in form_data.items():
                if v:
                    setattr(recipe, k, v)
            recipe.save()
            return HttpResponseRedirect(reverse('recipes:recipes_recipe', args=(category, recipe)))

    elif request.method == 'POST' and request.is_ajax and 'delete_recipe' in str(request.POST):
        if int(request.POST['confirmation']):
            recipe.delete()
            next_recipe = Recipe.objects.first()
            if next_recipe:
                return HttpResponseRedirect(reverse('recipes:recipes_recipe', args=(next_recipe.category, next_recipe.name)))
            else:
                return HttpResponseRedirect(reverse('recipes:recipes_cat', args=(recipe.category,)))
        else:
            return HttpResponseRedirect(reverse('recipes:recipes_recipe', args=(recipe.category, recipe.name)))

    elif request.method == 'POST' and request.is_ajax and 'checked_ids' in str(request.POST):
        print('ajax checked_ids')
        to_delete = request.POST['checked_ids'].split(',')
        if to_delete[0]:
            for item in to_delete:
                product = Product.objects.get(name=item)
                Amount.objects.filter(product=product.id).filter(recipe=recipe.id).delete()
        return HttpResponseRedirect(reverse('recipes:recipes_recipe', args=(recipe.category, recipe.name)))

    context['form_edit_recipe'] = EditRecipe()
    context['form_add_to_recipe'] = AddToRecipe()
    ingredients = Amount.objects.filter(recipe=recipe)

    product_data = recipe_data(ingredients)
    context['product_table'] = product_data['table_data']

    price = recipe.price.__round__(2)
    cost = product_data['total_cost'].__round__(2)
    profit = (price - cost).__round__(2)
    pct_margin = (100*(profit / price)).__round__(2) if price > 0 else 0

    context['product_data'] = {'price': price, 'cost': cost, 'profit': profit, 'margin': pct_margin,
                               'author': recipe.author, 'grammage': recipe.grammage}
    return render(request, 'recipes/recipes_recipe.html', context=context)


