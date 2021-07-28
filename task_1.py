"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1
Предприятия, с прибылью ниже среднего значения: Фирма_2
"""

from collections import namedtuple

company = namedtuple('comp_profit', 'name quarter_1 quarter_2 quarter_3 quarter_4')

count = int(input('Введите количество предприятий для расчета прибыли: '))

company_lst = []
for i in range(count):
    name = input('Введите название предприятия: ')
    profit = input('через пробел введите прибыль данного предприятия \n'
                   'за каждый квартал (всего 4 квартала): ').split(' ')
    profit = [int(i) for i in profit]
    company_lst.append(company(
        name=name,
        quarter_1=profit[0],
        quarter_2=profit[1],
        quarter_3=profit[2],
        quarter_4=profit[3]
    ))

aver_year_profit = 0
for el in company_lst:
    aver_year_profit += (el.quarter_1 + el.quarter_2 + el.quarter_3 + el.quarter_4) / 4
aver_year_profit /= count

print(f'Средняя годовая прибыль всех предприятий: {aver_year_profit}')

over_year_profit = [el.name for el in company_lst if
                    (el.quarter_1 + el.quarter_2 + el.quarter_3 + el.quarter_4) / 4 > aver_year_profit]
under_year_profit = [el.name for el in company_lst if
                     (el.quarter_1 + el.quarter_2 + el.quarter_3 + el.quarter_4) / 4 < aver_year_profit]

print(f'Предприятия, с прибылью выше среднего значения: {", ".join(over_year_profit)}')
print(f'Предприятия, с прибылью ниже среднего значения: {", ".join(under_year_profit)}')
