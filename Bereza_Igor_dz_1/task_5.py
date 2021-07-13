"""
Задание 5.
Задание на закрепление навыков работы со стеком
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.
После реализации структуры, проверьте ее работу на различных сценариях
Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""


class PlatesStackClass:
    def __init__(self, max_stack_size):
        self.elems = [[]]
        self.max_stack_size = max_stack_size

    def is_empty(self):
        return self.elems == [[]]

    def get_index(self):
        if len(self.elems) - 1 < 0:
            index = 0
        else:
            index = len(self.elems) - 1
        return index

    def push_in(self, el):
        index = self.get_index()
        if len(self.elems[index]) < self.max_stack_size:
            self.elems[index].append(el)
        else:
            self.elems.append([])
            self.elems[index + 1].append(el)
        return el

    def pop_out(self):
        index = self.get_index()
        if self.elems[index]:
            plate_out = self.elems[index].pop()
            if not self.elems[index] and index != 0:
                self.elems.pop()
        else:
            plate_out = 'Тарелок нет. Брать нечего.'
        return plate_out

    def get_val(self):
        index = self.get_index()
        if not self.elems[index]:
            return 'Тарелок нет'
        else:
            return self.elems[index][-1]

    def stack_size(self):
        return len(self.elems)


plates = PlatesStackClass(2)
# Проверка на пустой стек
print('Проверка на пустой стек:')
print('--------------------------------------------')
print(f'Стопка пустая? {"Да" if plates.is_empty() else "Нет"}')
print(f'Последняя тарелка в стопе: {plates.get_val()}')
print(f'Берём тарелку из стопы: {plates.pop_out()}')
print(f'Размер стека: {plates.stack_size()}')
print('--------------------------------------------')
print()
# Проверка на заполнение стека
print('Проверка на заполнение стека:')
print('--------------------------------------------')
for i in range(1, 6):
    plate = 'Тарелка_' + str(i)
    print(f'Помещаем тарелку в стопу: {plates.push_in(plate)}')
    print(f'Последняя тарелка в стопе: {plates.get_val()}')
    print(f'Размер стека: {plates.stack_size()}')
print(f'Стопка пустая? {"Да" if plates.is_empty() else "Нет"}')
print('--------------------------------------------')
print()
# Проверка на извлечение элементов из стека
print('Проверка на извлечение элементов из стека:')
print('--------------------------------------------')
for i in range(6):
    print(f'Берём тарелку из стопы: {plates.pop_out()}')
    print(f'Последняя тарелка в стопе: {plates.get_val()}')
    print(f'Размер стека: {plates.stack_size()}')
print(f'Стопка пустая? {"Да" if plates.is_empty() else "Нет"}')
print('--------------------------------------------')
