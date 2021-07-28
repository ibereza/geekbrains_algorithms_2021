"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit
from random import randint

standard_dict = {}
ordered_dict = OrderedDict()

standard_dict_append = """
for i in range(10000):
    standard_dict[i] = i"""

ordered_dict_append = """
for i in range(10000):
    ordered_dict[i] = i"""

print(timeit(standard_dict_append, globals=globals(), number=1000))  # 0.7295028
print(timeit(ordered_dict_append, globals=globals(), number=1000))  # 1.0232531
"""
Операция создания стандартного словаря выполняется быстрее, чем OrderedDict
"""

standard_dict_read = """
for i in range(10000):
    _ = standard_dict[randint(0, 9999)]"""

ordered_dict_read = """
for i in range(10000):
    _ = ordered_dict[randint(0, 9999)]"""

print(timeit(standard_dict_read, globals=globals(), number=100))  # 0.9908355000000002
print(timeit(ordered_dict_read, globals=globals(), number=100))  # 0.9116098999999998
"""
Получение значений из стандартного словаря незначительно дольше,
чем OrderedDict
"""

standard_dict_popitem = """
for i in range(0, 100):
    _ = standard_dict.popitem()"""

ordered_dict_popitem = """
for i in range(0, 100):
    _ = ordered_dict.popitem()
"""

print(timeit(standard_dict_popitem, globals=globals(), number=100))  # 0.0008128999999996722
print(timeit(ordered_dict_popitem, globals=globals(), number=100))   # 0.0014791000000000665
"""
Получение и удаление значений из стандартного словаря выполнилось быстрее,
чем из OrderedDict
"""

"""
По результатам замеров, можно сказать, что для версии Python 3.9
нет необходимости использовать OrderedDict, стандартный словарь
прекрасно справляется со своими задачами
"""
