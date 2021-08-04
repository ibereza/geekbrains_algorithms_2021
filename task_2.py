from random import random
from timeit import timeit


def merge_sort(arr):
    """
    Функция рекурсивно разбивает массив на две части
    и возвращает функцию объединения массивов
    """
    if len(arr) <= 1:
        return arr

    middle_arr = len(arr) // 2

    left_arr = merge_sort(arr[:middle_arr])
    right_arr = merge_sort(arr[middle_arr:])

    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    """
    Функция объединения двух массивов
    с сортировкой по возрастанию элементов
    """
    sorted_arr = []
    left_arr_index = right_arr_index = 0
    left_arr_len, right_arr_len = len(left_arr), len(right_arr)

    for _ in range(left_arr_len + right_arr_len):
        if left_arr_index < left_arr_len and right_arr_index < right_arr_len:
            if left_arr[left_arr_index] <= right_arr[right_arr_index]:
                sorted_arr.append(left_arr[left_arr_index])
                left_arr_index += 1
            else:
                sorted_arr.append(right_arr[right_arr_index])
                right_arr_index += 1
        else:
            if left_arr_index == left_arr_len:
                sorted_arr.append(right_arr[right_arr_index])
                right_arr_index += 1
            else:
                sorted_arr.append(left_arr[left_arr_index])
                left_arr_index += 1

    return sorted_arr


num_list = [random() * 50 for _ in range(10)]
print(num_list)
print(merge_sort(num_list[:]))

for num_cycles in (10, 100, 1000):
    num_list = [random() * 50 for _ in range(num_cycles)]
    print(f'Массив из {num_cycles} элементов:')
    print(
        timeit(
            'merge_sort(num_list[:])',
            globals=globals(),
            number=1000))

"""
Массив из 10 элементов:
0.015495000000000002
Массив из 100 элементов:
0.22668300000000002
Массив из 1000 элементов:
3.1013447

По результатам замеров видно, что при увеличении массива время выполнения изменяется не существенно.
Это говорит о том, что скорость близка к O(n log n).
"""
