from django import forms
from .models import IncomeStatement

from cookbookdb import settings

input_formats=settings.DATE_INPUT_FORMATS


class AddIncomeStatement(forms.Form):
    sales = forms.FloatField(label='Sprzedaż razem', required=False, max_value=100000000)
    n_of_sales = forms.IntegerField(label='Liczba paragonów', required=False, max_value=100000000)

    rent = forms.FloatField(label='Czynsz', required=False, max_value=10000000)
    water = forms.FloatField(label='Woda', required=False, max_value=100000000)
    gas = forms.FloatField(label='Gaz', required=False, max_value=100000000)
    electricity = forms.FloatField(label='Prąd', required=False, max_value=100000000)
    garbage = forms.FloatField(label='Śmieci', required=False, max_value=100000000)
    net_phone = forms.FloatField(label='Internet/telefon', required=False, max_value=100000000)
    security = forms.FloatField(label='Ochrona', required=False, max_value=100000000)
    accounting_hr = forms.FloatField(label='Księgowość/kadry', required=False, max_value=100000000)
    marketing = forms.FloatField(label='Marketing/reklama', required=False, max_value=100000000)
    terminal_fee = forms.FloatField(label='Prowizja terminal', required=False, max_value=100000000)
    chemicals = forms.FloatField(label='Chemia', required=False, max_value=100000000)
    equipment = forms.FloatField(label='Wyposażenie restauracji', required=False, max_value=100000000)
    repairs = forms.FloatField(label='Naprawy/serwisy', required=False, max_value=100000000)
    license_fees = forms.FloatField(label='Opłaty, pozwolenia, koncesje', required=False, max_value=100000000)
    training = forms.FloatField(label='Badania/ szkolenia', required=False, max_value=100000000)
    dress = forms.FloatField(label='Stroje służbowe', required=False, max_value=100000000)
    fuel = forms.FloatField(label='Paliwo', required=False, max_value=100000000)
    office_equipment = forms.FloatField(label='Materiały biurowe', required=False, max_value=100000000)
    laundry = forms.FloatField(label='Pralnia/sprzątanie', required=False, max_value=100000000)

    kitchen = forms.FloatField(label='Koszt surowca kuchnia', max_value=100000000)
    bar = forms.FloatField(label='Koszt surowca bar', max_value=100000000)
    events = forms.FloatField(label='Koszt surowca bankiety/eventy', max_value=100000000)
    employee_meals = forms.FloatField(label='Koszt surowca posiłki pracownicze', max_value=100000000)
    snacks = forms.FloatField(label='Koszt surowca poczęstunki', max_value=100000000)

    kitchen_eom_stock = forms.FloatField(label='Stan magazynu na koniec miesiąca: kuchnia', max_value=100000000)
    bar_eom_stock = forms.FloatField(label='Stan magazynu na koniec miesiąca: bar', max_value=100000000)

    salaries = forms.FloatField(label='Wynagrodzenia netto', max_value=100000000)
    zus = forms.FloatField(label='ZUS', max_value=100000000)
    tax = forms.FloatField(label='Podatek', max_value=100000000)
    bonuses = forms.FloatField(label='Premie/prowizje', max_value=100000000)
    other = forms.FloatField(label='Inne koszty personelu', max_value=100000000)

    n_of_working_days = forms.IntegerField(label='Liczba dni roboczych w miesiącu', max_value=31)
    n_of_workhours = forms.IntegerField(label='Liczba godzin przepracowanych', max_value=100000)








