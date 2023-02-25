
from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.products, name='products'),
    path('<category>', views.products_category, name='products_category'),
]
