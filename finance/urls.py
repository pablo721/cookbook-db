from django.contrib import admin
from django.urls import path

from . import views

app_name = 'finance'
urlpatterns = [
    path('', views.finance, name='finance'),
    path('rachunek_zyskow_i_strat', views.new_income_statement, name='new_income_statement'),
]


