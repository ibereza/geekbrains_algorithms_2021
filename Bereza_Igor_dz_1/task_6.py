"""
Задание 6.
Задание на закрепление навыков работы с очередью
Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""


class QueueClass:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def add_element(self, el):
        self.queue.insert(0, el)

    def extract_element(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)


class TaskBoardClass:
    def __init__(self):
        self.base_queue = QueueClass()
        self.rework_queue = QueueClass()
        self.solved_lst = []

    def to_base_queue(self, el):
        self.base_queue.add_element(el)

    def to_rework_queue(self):
        task = self.base_queue.extract_element()
        self.rework_queue.add_element(task)

    def from_rework_to_base(self):
        task = self.rework_queue.extract_element()
        self.base_queue.add_element(task)

    def end_task(self):
        task = self.base_queue.extract_element()
        self.solved_lst.append(task)

    def current_base_task(self):
        if self.base_queue.size() - 1 < 0:
            return 'Нет базовых задач'
        else:
            index = self.base_queue.size() - 1
            return self.base_queue.queue[index]

    def current_rework_task(self):
        if self.rework_queue.size() - 1 < 0:
            return 'Нет задач на доработку'
        else:
            index = self.rework_queue.size() - 1
            return self.rework_queue.queue[index]


task_board = TaskBoardClass()
# Смотрим текующую задачу (отсутствие задачи)
print(task_board.current_base_task())
# Создаём задачи
task_board.to_base_queue('Подточить карандаш')
task_board.to_base_queue('Спасти мир')
task_board.to_base_queue('Купить пива')
task_board.to_base_queue('Посмотреть футбол')
# Смотрим текующую задачу
print(task_board.current_base_task())
# Завершаем текущую задачу
task_board.end_task()
# Смотрим текующую задачу
print(task_board.current_base_task())
# Переносим текущую задачу в доработку
task_board.to_rework_queue()
# Смотрим текущую задачу в доработке
print(task_board.current_rework_task())
# Переносим из доработки в базовые задачи
task_board.from_rework_to_base()
# Смотрим текующую задачу в доработке (отсутствие задачи)
print(task_board.current_rework_task())
# Смотрим текующую задачу
print(task_board.current_base_task())
# Завершаем текущую задачу
task_board.end_task()
# Смотрим текующую задачу
print(task_board.current_base_task())
# Смотрим список выполненных задач
print(task_board.solved_lst)
