"""
При выполнении задания task_1_1.py использовал
профилирование памяти для функции с рекурсией.
Чтобы профилирование отработало не для каждого
рекурсионного вызова функции, а для функции в
целом, пришлось использовать функцию-обёртку:
"""

from memory_profiler import profile


@profile
def wrapper(num):
    def sum_numbers(count):
        return 0 if count == 0 else count + sum_numbers(count - 1)
    return sum_numbers(num)

