"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача:
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.
В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""

from collections import deque
from timeit import timeit
from random import randint

lst = []
lst_deque = deque()

lst_append = """
for i in range(10000):
    lst.append(i)"""

lst_deque_append = """
for i in range(10000):
    lst_deque.append(i)"""

print(timeit(lst_append, globals=globals(), number=1000))  # 0.7820958
print(timeit(lst_deque_append, globals=globals(), number=1000))  # 0.6320992
"""
Даже при обычном заполнении с конца списка deque отрабатывает быстрее
примерно на 24%.
"""

lst.clear()

lst_insert = """
for i in range(10000):
    lst.insert(0, i)"""

lst_deque_appendleft = """
for i in range(10000):
    lst_deque.appendleft(i)"""

print(timeit(lst_insert, globals=globals(), number=10))  # 2.7596993999999997
print(timeit(lst_deque_appendleft, globals=globals(), number=10))  # 0.006074100000000193
"""
при операции вставки элементов в начало списка, скорость наполнения deque
на несколько порядков выше скорости наполнения простого списка.
Если для deque.appendleft выставить значения замеров скорости как и для
deque.append, то можно увидеть, что эти операции по скорости практически
не отличаются. То есть для deque нет разницы выполнять вставку в начало
списка или в его конец.
"""

lst.clear()

for i in range(100000):
    lst.append(i)
    lst_deque.append(i)

lst_pop = """
for i in range(1000):
    lst.pop(0)"""

lst_deque_popleft = """
for i in range(1000):
    lst_deque.popleft()"""

print(timeit(lst_pop, globals=globals(), number=100))  # 1.6178922
print(timeit(lst_deque_popleft, globals=globals(), number=100))  # 0.007845800000000125
"""
При извлечении элементов из начала списка, deque так же работает
на несколько порядков быстрее.
"""

lst.clear()

for i in range(10000):
    lst.append(i)
    lst_deque.append(i)

print(timeit('lst[randint(0, 9999)]', globals=globals()))  # 0.9237231999999995
print(timeit('lst_deque[randint(0, 9999)]', globals=globals()))  # 1.1894968000000006
"""
А вот операция случайного доступа к списку для обычного списка
выполняется быстрее.
"""

"""
Можно сделать вывод, что операции маипулирования списками с deque выполняются
значительно быстрее, чем операции с обычным списком.
Операция доступа к списку быстрее выполняется с обычным списком.
"""
