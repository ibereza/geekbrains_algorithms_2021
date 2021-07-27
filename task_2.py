"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
__mul__
__add__
Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
1. вариант
defaultdict(list)
int(, 16)
reduce
2. вариант
class HexNumber:
    __add__
    __mul__
hx = HexNumber
hx + hx
hex()
"""

from collections import defaultdict

numbers = defaultdict(list)

hex_number_1 = input('Введтите первое шестнадцетиричное число: ')
numbers[hex_number_1] = list(hex_number_1)
hex_number_2 = input('Введтите второе шестнадцетиричное число: ')
numbers[hex_number_2] = list(hex_number_2)

hex_numbers = [int(''.join(el), 16) for el in numbers.values()]

hex_sum = list(hex(hex_numbers[0] + hex_numbers[1])[2:].upper())
print(f'Сумма чисел: {hex_sum}')

hex_multiple = list(hex(hex_numbers[0] * hex_numbers[1])[2:].upper())
print(f'Произведение чисел: {hex_multiple}')


class HexAddMul:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def __add__(self, other):
        return list(hex(int(self.number_1, 16) + int(other.number_2, 16))[2:].upper())

    def __mul__(self, other):
        return list(hex(int(self.number_1, 16) * int(other.number_2, 16))[2:].upper())


hex_sum = HexAddMul(hex_number_1, hex_number_2) + HexAddMul(hex_number_1, hex_number_2)
print(f'Сумма чисел (ООП): {hex_sum}')

hex_multiple = HexAddMul(hex_number_1, hex_number_2) * HexAddMul(hex_number_1, hex_number_2)
print(f'Сумма чисел (ООП): {hex_multiple}')
