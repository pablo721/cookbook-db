from django.db import models


# Create your models here.


class IncomeStatement(models.Model):
    date = models.DateField(verbose_name='Data', null=True, unique=True, blank=False)
    sales = models.FloatField(blank=False, null=True, verbose_name='Sprzedaż razem')
    n_of_sales = models.IntegerField(blank=True, null=True, verbose_name='Liczba paragonów')

    rent = models.FloatField(blank=True, null=True, verbose_name='Czynsz')
    water = models.FloatField(blank=True, null=True, verbose_name='Woda')
    gas = models.FloatField(blank=True, null=True, verbose_name='Gaz')
    electricity = models.FloatField(blank=True, null=True, verbose_name='Prąd')
    garbage = models.FloatField(blank=True, null=True, verbose_name='Śmieci')
    net_phone = models.FloatField(blank=True, null=True, verbose_name='Internet/telefon')
    security = models.FloatField(blank=True, null=True, verbose_name='Ochrona')
    accounting_hr = models.FloatField(blank=True, null=True, verbose_name='Księgowość/kadry')
    marketing = models.FloatField(blank=True, null=True, verbose_name='Marketing/reklama')
    terminal_fee = models.FloatField(blank=True, null=True, verbose_name='Prowizja terminal')
    chemicals = models.FloatField(blank=True, null=True, verbose_name='Chemia')
    equipment = models.FloatField(blank=True, null=True, verbose_name='Wyposażenie restauracji')
    repairs = models.FloatField(blank=True, null=True, verbose_name='Naprawy/serwisy')
    license_fees = models.FloatField(blank=True, null=True, verbose_name='Opłaty, pozwolenia, koncesje')
    training = models.FloatField(blank=True, null=True, verbose_name='Badania/szkolenia')
    dress = models.FloatField(blank=True, null=True, verbose_name='Stroje służbowe')
    fuel = models.FloatField(blank=True, null=True, verbose_name='Paliwo')
    office_equipment = models.FloatField(blank=True, null=True, verbose_name='Materiały biurowe')
    laundry = models.FloatField(blank=True, null=True, verbose_name='Pralnia/sprzątanie')

    kitchen = models.FloatField(blank=True, null=True, verbose_name='Koszt surowca kuchnia')
    bar = models.FloatField(blank=True, null=True, verbose_name='Koszt surowca bar')
    events = models.FloatField(blank=True, null=True, verbose_name='Koszt surowca bankiety/eventy')
    employee_meals = models.FloatField(blank=True, null=True, verbose_name='Koszt surowca posiłki pracownicze')
    snacks = models.FloatField(blank=True, null=True, verbose_name='Koszt surowca poczęstunki')

    kitchen_eom_stock = models.FloatField(blank=True, null=True, verbose_name='Stan magazynu na koniec miesiąca: kuchnia')
    bar_eom_stock = models.FloatField(blank=True, null=True, verbose_name='Stan magazynu na koniec miesiąca: bar')

    salaries = models.FloatField(blank=True, null=True, verbose_name='Wynagrodzenia netto')
    zus = models.FloatField(blank=True, null=True, verbose_name='ZUS')
    tax = models.FloatField(blank=True, null=True, verbose_name='Podatek')
    bonuses = models.FloatField(blank=True, null=True, verbose_name='Premie/prowizje')
    other = models.FloatField(blank=True, null=True, verbose_name='Inne koszty personelu')

    n_of_working_days = models.IntegerField(blank=True, null=True, verbose_name='Liczba dni roboczych w miesiącu')
    n_of_workhours = models.IntegerField(blank=True, null=True, verbose_name='Liczba godzin przepracowanych')



