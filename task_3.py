"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.
Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""


string = 'papa'
unique_substrings_hash = set()
for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        substring = string[i:j]
        if substring != string:
            substring_hash = hash(substring)
            unique_substrings_hash.add(substring_hash)
print(f'Кол-во уникальных подстрок: {len(unique_substrings_hash)}')
