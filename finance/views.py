from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core import serializers
from .forms import AddIncomeStatement
from .models import IncomeStatement
from .utils import TABLE_INDEX, calculate_financials, calculate_aggregate_costs, get_sorted_statement
import datetime

# Create your views here.


@login_required
def finance(request):
    data = []
    financial_statements = IncomeStatement.objects.values()

    for statement in financial_statements:
        financials, costs = calculate_financials(statement)
        sorted_statement = get_sorted_statement(statement, costs, financials)
        data.append(sorted_statement)

    return render(request, 'finance/finance.html', context={'data': data, 'fields': TABLE_INDEX})


@login_required
def new_income_statement(request):
    if request.method == 'POST':
        data = AddIncomeStatement(request.POST)
        if data.is_valid():
            statement = data.cleaned_data
            statement['date'] = datetime.date(year=int(request.POST['date_input'].split('-')[0]),
                                          month=int(request.POST['date_input'].split('-')[1]),
                                              day=30)
            obj = IncomeStatement.objects.create(**statement)
            obj.save()
        else:
            print(data.errors)
        return HttpResponseRedirect(reverse('finance:finance'))
    else:
        form = AddIncomeStatement()
        return render(request, 'finance/new_income_statement.html', context={'form': form})



