
CATEGORIES = {'date': ['date'],
              'sales': ['sales'],
              'inventory': ['kitchen_eom_stock', 'bar_eom_stock'],
              'costs': {
              'operating_costs': ['rent', 'water', 'gas', 'electricity', 'garbage', 'net_phone', 'security',
                                  'accounting_hr', 'marketing', 'terminal_fee', 'chemicals', 'equipment', 'repairs',
                                  'license_fees', 'training', 'dress', 'fuel', 'office_equipment', 'laundry'],
              'materials_costs': ['kitchen', 'bar', 'events', 'employee_meals', 'snacks'],
              'staff_costs': ['salaries', 'zus', 'tax', 'bonuses', 'other']},
              'other': ['n_of_sales', 'n_of_working_days', 'n_of_workhours']}

TABLE_INDEX = ['Data', 'Sprzedaż razem', 'Koszt surowca', 'Koszt personelu', 'Koszty operacyjne',
               'Zysk EBITDA', 'Srednia sprzedaż dzienna', 'Średni rachunek', 'Liczba paragonów',
               'Koszty operacyjne restauracji',
               'Czynsz', 'Woda', 'Gaz', 'Prąd', 'Śmieci', 'Internet/telefon', 'Ochrona', 'Księgowość/kadry',
                'Marketing/reklama', 'Prowizja terminal', 'Chemia', 'Wyposażenie restauracji', 'Naprawy/serwisy',
                'Opłaty, pozwolenia, koncesje', 'Badania/szkolenia', 'Strone służbowe', 'Paliwo', 'Materiały biurowe',
                'Pralnia/sprzątanie', 'Suma',
               'Koszty surowca',
                'Koszt surowca kuchnia', 'Koszt surowca bar', 'Koszt surowca bankiety/eventy',
                'Koszt surowca posiłki pracownicze', 'Koszt surowca poczęstunki',
                'Stan magazynu na koniec miesiąca: kuchnia', 'Stan magazynu na koniec miesiąca: bar', 'Suma',
                'Koszty personelu',
                'Wynagrodzenia netto', 'ZUS', 'Podatek', 'Premie/prowizje', 'Inne koszty personelu',
                'Liczba dni roboczych w miesiącu', 'Liczba godzin przepracowanych',
                'Obrót/roboczogodzinę pracy', 'Średni koszt roboczogodziny', 'Suma']

CALCULATED_VALUES = ['Stan magazynu na koniec miesiąca',
                     'Koszty operacyjne', 'Koszty surowca', 'Koszty personelu', 'Koszty całkowite',
                     'Zysk EBITDA',
                     'Średnia sprzedaż dzienna', 'Średni rachunek', 'Obrót/roboczogodzinę pracy',
                     'Średni koszt roboczogodziny']


def get_cost_category(position):
    for k, v in CATEGORIES['costs'].items():
        if position in v:
            return k
    return False


def calculate_aggregate_costs(statement_data):
    result = {'materials_costs': 0, 'staff_costs': 0, 'operating_costs': 0}
    for k, v in statement_data.items():
        category = get_cost_category(k)
        if category:
            result[category] += v
    result['materials_costs'] -= (statement_data['kitchen_eom_stock'] + statement_data['bar_eom_stock'])
    #result['total_cost'] = sum(list(result.values()))
    return result


def calculate_financials(statement_data):
    costs = calculate_aggregate_costs(statement_data)
    total_cost = sum(costs.values())
    result = dict()
    result['ebitda'] = (statement_data['sales'] - sum(costs.values())).__round__(2)
    result['avg_daily_sales'] = (statement_data['sales'] / statement_data['n_of_working_days']).__round__(2)
    result['avg_bill'] = (statement_data['sales'] / statement_data['n_of_sales']).__round__(2)
    result['sales_to_workhours'] = (statement_data['sales'] / statement_data['n_of_workhours']).__round__(2)
    result['avg_cost_of_workhour'] = (total_cost / statement_data['n_of_workhours']).__round__(2)
    return result, costs


def get_sorted_statement(statement_data, aggregate_costs, calculated_data):
    values = [
        statement_data['date'], statement_data['sales'],
        aggregate_costs['materials_costs'], aggregate_costs['staff_costs'], aggregate_costs['operating_costs'],
        calculated_data['ebitda'], calculated_data['avg_daily_sales'], calculated_data['avg_bill'],
        statement_data['n_of_sales'],
        '',
        statement_data['rent'], statement_data['water'], statement_data['gas'], statement_data['electricity'],
        statement_data['garbage'], statement_data['net_phone'], statement_data['security'],
        statement_data['accounting_hr'], statement_data['marketing'], statement_data['terminal_fee'],
        statement_data['chemicals'], statement_data['equipment'], statement_data['repairs'],
        statement_data['license_fees'], statement_data['training'], statement_data['dress'], statement_data['fuel'],
        statement_data['office_equipment'], statement_data['laundry'],
        aggregate_costs['operating_costs'],
        '',
        statement_data['kitchen'], statement_data['bar'], statement_data['events'], statement_data['employee_meals'],
        statement_data['snacks'],
        statement_data['kitchen_eom_stock'], statement_data['bar_eom_stock'],
        aggregate_costs['materials_costs'],
        '',
        statement_data['salaries'], statement_data['zus'], statement_data['tax'],
        statement_data['bonuses'], statement_data['other'],
        statement_data['n_of_working_days'], statement_data['n_of_workhours'], calculated_data['sales_to_workhours'],
        calculated_data['avg_cost_of_workhour'],
        aggregate_costs['staff_costs'],
        ]

    percentages = ['%', 100]

    for cost in aggregate_costs.values():
        percentages.append((100 * cost / statement_data['sales']).__round__(2))

    percentages.append((100 * calculated_data['ebitda'] / statement_data['sales']).__round__(2))
    percentages += 3*['']

    for category, costs in CATEGORIES['costs'].items():
        percentages.append('')
        for cost in costs:
            percentages.append((100 * statement_data[cost] / aggregate_costs[category]).__round__(2))
        if category == 'materials_costs':
            empty_rows = 2
        elif category == 'staff_costs':
            empty_rows = 4
        else:
            empty_rows = 0

        percentages += empty_rows * [''] + [100]



    return values, percentages





