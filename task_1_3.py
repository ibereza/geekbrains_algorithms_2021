"""
Из урока 5, задача 2
"""

from collections import defaultdict

from pympler import asizeof


class HexAddMul:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def __add__(self, other):
        return list(hex(int(self.number_1, 16) + int(other.number_2, 16))[2:].upper())

    def __mul__(self, other):
        return list(hex(int(self.number_1, 16) * int(other.number_2, 16))[2:].upper())


class HexAddMulSlots:
    __slots__ = ('number_1', 'number_2')

    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def __add__(self, other):
        return list(hex(int(self.number_1, 16) + int(other.number_2, 16))[2:].upper())

    def __mul__(self, other):
        return list(hex(int(self.number_1, 16) * int(other.number_2, 16))[2:].upper())


numbers = defaultdict(list)

hex_number_1 = input('Введтите первое шестнадцетиричное число: ')
numbers[hex_number_1] = list(hex_number_1)
hex_number_2 = input('Введтите второе шестнадцетиричное число: ')
numbers[hex_number_2] = list(hex_number_2)

hex_obj = HexAddMul(hex_number_1, hex_number_2)

hex_sum = hex_obj + hex_obj
print(f'Сумма чисел (ООП): {hex_sum}')

hex_multiple = hex_obj * hex_obj
print(f'Сумма чисел (ООП): {hex_multiple}')

hex_obj_slots = HexAddMulSlots(hex_number_1, hex_number_2)

hex_sum = hex_obj + hex_obj
print(f'Сумма чисел (ООП Slots): {hex_sum}')

hex_multiple = hex_obj * hex_obj
print(f'Сумма чисел (ООП Slots): {hex_multiple}')

print(f'Размер области хранения переменных для объекта класса HexAddMul: {asizeof.asizeof(hex_obj)}')
print(f'Размер области хранения переменных для объекта класса HexAddMulSlots: {asizeof.asizeof(hex_obj_slots)}')

"""
Размер области хранения переменных для объекта класса HexAddMul: 392
Размер области хранения переменных для объекта класса HexAddMulSlots: 160

В классе HexAddMul для хранения переменных используется словарь.
В классе HexAddMulSlots для уменьшения выделяемой памяти под переменные,
вместо словаря я использовал слоты в виде кортежа.
Благодаря этому произошло уменьшение памяти с 392 до 160. 
"""
