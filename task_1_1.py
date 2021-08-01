"""
Из урока 2, задача 7.
"""

from memory_profiler import profile


@profile
def wrapper(num):
    def sum_numbers(count):
        return 0 if count == 0 else count + sum_numbers(count - 1)
    return sum_numbers(num)


@profile
def sum_numbers_cycle(num):
    sum_num = 0
    for i in range(1, num + 1):
        sum_num += i
    return sum_num


print(f'{wrapper(900)} = {int(900 * (900 + 1) / 2)}')
print(f'{sum_numbers_cycle(900)} = {int(900 * (900 + 1) / 2)}')

"""
Результат выполнения функции реализованную через рекурсию:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     4     19.4 MiB     19.4 MiB           1   @profile
     5                                         def wrapper(num):
     6     21.1 MiB      1.8 MiB         902       def sum_numbers(count):
     7     21.1 MiB      0.0 MiB         901           return 0 if count == 0 else count + sum_numbers(count - 1)
     8     21.1 MiB      0.0 MiB           1       return sum_numbers(num)
     
Результат выполнения функции реализованную через цикл:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     21.2 MiB     21.2 MiB           1   @profile
    12                                         def sum_numbers_cycle(num):
    13     21.2 MiB      0.0 MiB           1       sum_num = 0
    14     21.2 MiB      0.0 MiB         901       for i in range(1, num + 1):
    15     21.2 MiB      0.0 MiB         900           sum_num += i
    16     21.2 MiB      0.0 MiB           1       return sum_num

При использовании рекурсии для стека вызовов необходимо было дополнительное выделение 1.8 MiB памяти.
При использовании цикла дополнительное выделение памяти не требуется, вычисления происходят
для одной переменной sum_num.
"""
