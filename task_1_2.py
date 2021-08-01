"""
Из урока 4, задача 1
"""
from memory_profiler import memory_usage
from timeit import default_timer


def measuring_time_mem(func):
    """
    Декоратор для замера времени выполнения функции
    и количества используемой памяти
    """
    def wrapper(arg):
        start_time = default_timer()
        start_mem = memory_usage()[0]
        result = func(arg)
        print(f'Для функции {func.__name__}:')
        print(f'Время выполнения: {default_timer() - start_time} cек.')
        print(f'Использовано {memory_usage()[0] - start_mem} MiB памяти')
        return result
    return wrapper


@measuring_time_mem
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@measuring_time_mem
def func_2(nums):
    return filter(lambda x: x % 2 == 0, nums)


nums_lst = [i for i in range(1000000)]
func_1(nums_lst)
func_2(nums_lst)

"""
Для функции func_1:
Время выполнения: 0.20699859999999998 cек.
Использовано 18.3125 MiB памяти

Для функции func_2:
Время выполнения: 0.10333599999999998 cек.
Использовано 0.0 MiB памяти

Для функции func_1 в качестве возвращаемого значения используется список.
Для формирования списка необходима память. Поэтому func_1 использует 
определённое кол-во памяти.

Если нет необходимости обязательно возвращать список (например, в дальнейшем
будет производится обработка списка с помощью итерации), то в качестве 
возвращаемого значения можно использовать итератор (в функции func_2
я использовал функцию filter, которая возвращает итерируемый объект).
В результате не используется дополнительная память, к тому же, при очень
больших списках, время выполнения функции уменьшается.
"""
