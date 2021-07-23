"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым!
"""

from timeit import timeit
from collections import Counter

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)
    max_2 = max(new_array)

    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    """
    Оптимизировал функцию func_1.
    Уменьшил кол-во итераций за счет применения кортежа
    вместо списка с повторяющимися элементами.
    """
    m = 0
    num = 0
    for i in set(array):
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_4():
    """
    Использовал функцию max()
    """
    num_max_count = max(array, key=array.count)
    count = array.count(num_max_count)
    return f'Чаще всего встречается число {num_max_count}, ' \
           f'оно появилось в массиве {count} раз(а)'


def func_5():
    """
    Использовал коллекцию Counter
    """
    max_count = Counter(array).most_common(1)
    return f'Чаще всего встречается число {max_count[0][0]}, ' \
           f'оно появилось в массиве {max_count[0][1]} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())

print(f"func_1: {timeit('func_1()', globals=globals())}")  # 1.3104392999999999
print(f"func_2: {timeit('func_2()', globals=globals())}")  # 1.9664962999999998
print(f"func_3: {timeit('func_3()', globals=globals())}")  # 1.1512883
print(f"func_4: {timeit('func_4()', globals=globals())}")  # 1.4996323
print(f"func_5: {timeit('func_5()', globals=globals())}")  # 4.7947284

"""
Самой быстрой оказалась функция 3 за счет оптимизации кол-ва итераций через кортеж.
Неожиданно для меня коллекция Counter дала существенно худший результат по скорости выполнения.
"""
