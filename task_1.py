"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def calc():
    sign = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    while sign not in '+-*/0' or len(sign) > 1:
        print('Некорректный ввод!')
        sign = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if sign == '0':
        return
    number_1 = input('Введите первое число: ')
    while not number_1.isdigit():
        print('Некорректный ввод! Можно вводить только целые числа.')
        number_1 = input('Введите первое число: ')
    number_1 = int(number_1)
    number_2 = input('Введите второе число: ')
    while not number_2.isdigit():
        print('Некорректный ввод! Можно вводить только целые числа.')
        number_2 = input('Введите второе число: ')
    number_2 = int(number_2)
    if sign == '+':
        result = number_1 + number_2
    elif sign == '-':
        result = number_1 - number_2
    elif sign == '*':
        result = number_1 * number_2
    else:
        if number_2 == 0:
            result = 'На ноль делить нельзя!'
        else:
            result = number_1 / number_2
    print(f'Ваш результат: {result}')
    calc()


calc()
