"""
Задание 5.**
Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).
Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)
Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма.
Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснование результатам.
"""

from timeit import timeit


def simple(i):
    """
    Без использования «Решета Эратосфена»
    O(n^2)
    """
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def calc_prime_num(num):
    """
    Использовано "Решето Эратосфена"
    O(n * log(log(n)))
    """
    arr = [2, 3]
    current_num = 4

    while len(arr) < num:
        if current_num % 2 != 0 and current_num % 3 != 0:
            temp = 4
            while temp * temp <= current_num:
                if current_num % temp == 0:
                    break
                temp += 1
            if temp * temp > current_num:
                arr.append(current_num)
        current_num += 1

    return arr[num - 1]


print(f"simple(10): {timeit('simple(10)', globals=globals(), number=100000)}")
# simple(10): 1.6391079
print(simple(10))  # 29
print(f"calc_prime_num(10): {timeit('calc_prime_num(10)', globals=globals(), number=100000)}")
# calc_prime_num(10): 0.5126336999999999
print(calc_prime_num(10))  # 29

print(f"simple(100): {timeit('simple(100)', globals=globals(), number=1000)}")
# simple(100): 2.2223193
print(simple(100))  # 541
print(f"calc_prime_num(100): {timeit('calc_prime_num(100)', globals=globals(), number=1000)}")
# calc_prime_num(100): 0.22393860000000032
print(calc_prime_num(100))  # 541

print(f"simple(1000): {timeit('simple(1000)', globals=globals(), number=10)}")
# simple(1000): 3.1338692999999997
print(simple(1000))  # 7919
print(f"calc_prime_num(1000): {timeit('calc_prime_num(1000)', globals=globals(), number=10)}")
# calc_prime_num(1000): 0.08214629999999978
print(calc_prime_num(1000))  # 7919

"""
Без использования "Решета Эратосфена" идет двойной перебор элементов, 
в результате получается квадратичная сложность O(n^2).
При использовании "Решета Эратосфена" за счет "отсеивания элементов"
значительно меньше элементов участвуют в переборе, получается
что-то вроде линейно-логарифмической сложности O(n * log(log(n))).
В результате, "Решето Эратосфена" даёт значительный выигрыш в скорости выполнения.
"""
