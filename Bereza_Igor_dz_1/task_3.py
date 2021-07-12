"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

companies_dict = {
    'JPMorgan Chase': 17.4,
    'General Electric': 11.6,
    'ExxonMobil': 30.5,
    'Berkshire Hathaway': 13.0,
    'Citigroup': 10.6,
    'AT&T': 19.9,
    'Chevron': 19.0,
    'Walmart': 16.4,
    'IBM': 14.8,
    'Procter & Gamble': 11.8,
    'Pfizer': 8.3,
    'Hewlett-Packard': 9.1,
    'Apple': 16.6,
    'Microsoft': 20.6,
    'Ford': 6.6,
    'Johnson & Johnson': 13.3,
    'Coca-Cola': 11.8
}


def max_profit_1(comp_dict):
    """
    Сложность: O(n^2) - квадратичная (цикл внутри цикла).
    """
    comp_dict = comp_dict.copy()  # O(n)
    max_dict = {}  # O(1)
    max_key = ''  # O(1)
    for i in range(3):  # O(1)
        for key, value in comp_dict.items():  # O(n)
            max_value = value  # O(1)
            max_key = key  # O(1)
            for key_iter in comp_dict.keys():  # O(n)
                if comp_dict[key_iter] > max_value:  # O(1)
                    max_value = comp_dict[key_iter]  # O(1)
                    max_key = key_iter  # O(1)
        max_dict.update({max_key: comp_dict.pop(max_key)})  # O(1)
    return max_dict  # O(1)


def max_profit_2(comp_dict):
    """
    Сложность: O(n log n) - линейно-логарифмическая (функция сортировки).

    Второй вариант эффективнее, так как при линейно-логарифмической сложности
    рост операций при увеличении кол-ва данных значительно меньше,
    чем у квадратичной сложности.
    """
    comp_dict = comp_dict.copy()  # O(n)
    max_dict = {}  # O(1)
    temp_dict = {value: key for key, value in comp_dict.items()}  # O(n)
    for key in sorted(temp_dict, reverse=True)[0:3]:  # O(n log n)
        max_dict.update({key: temp_dict[key]})  # O(1)
    max_dict = {value: key for key, value in max_dict.items()}  # O(n)
    return max_dict  # O(1)


print(max_profit_1(companies_dict))
print(max_profit_2(companies_dict))
