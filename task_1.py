"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    new_arr = []
    for i, el in enumerate(nums):
        if el % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_4(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


nums_lst = [i for i in range(1000)]

print(f"func_1: {timeit('func_1(nums_lst)', globals=globals(), number=10000)}")  # func_1: 0.7510935999999999
print(f"func_2: {timeit('func_2(nums_lst)', globals=globals(), number=10000)}")  # func_2: 0.6957283
print(f"func_3: {timeit('func_3(nums_lst)', globals=globals(), number=10000)}")  # func_3: 0.9304763000000003
print(f"func_4: {timeit('func_4(nums_lst)', globals=globals(), number=10000)}")  # func_4: 0.7251672

# func_2: вместо простого цикла используется list comprehension.
# функция выполняется быстрее.
# func_3: используется цикл, но в качестве генератора используется enumerate.
# время выполнения увеличилось, очевидно enumerate требует дополнительного времени.
# func_4: используется list comprehension с enumerate.
# выполняется быстрее, чем обычный цикл, но медленнее чем list comprehension с range(len())
