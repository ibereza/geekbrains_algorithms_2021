"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
Без аналитики задание считается не принятым
"""

from timeit import timeit
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    revers_num = int(''.join(reversed(str(enter_num))))
    return revers_num


print(timeit('revers_1(12345)', globals=globals()))  # 1.4084724
print(timeit('revers_2(12345)', globals=globals()))  # 0.9182081
print(timeit('revers_3(12345)', globals=globals()))  # 0.3304459999999998
print(timeit('revers_4(12345)', globals=globals()))  # 0.7436976

run('revers_1(12345)')
run('revers_2(12345)')
run('revers_3(12345)')
run('revers_4(12345)')

'''
Первая функция  - рекурсия, выполняется дольше всех.
Вторая - цикл, выполняется быстрее чем рекурсия, но медленнее встроенных функций.
Третья - срезы, встроенная функция, самое быстрое из четырех время выполнения.
Четвертая - с помощью функции reversed, быстрее чем пользовательские функции,
но меделенне среза.
Встроенные функции исполняются быстрее пользовательских.
'''
