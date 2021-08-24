# Написать два алгоритма нахождения i-го по счёту простого числа.
#
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.


# Используя алгоритм «Решето Эратосфена»
import cProfile


# Сложность: O(n log n)
# Время: 3.22 при 10000
# Время: 5.67 при 100000

# Используя алгоритм «Решето Эратосфена»
def with_reshet():
    n = int(input("вывод простых чисел до числа ... "))
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0

    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    print(b)


# Сложность: O(n^2)
# Время: 3.32 при 10000
# Время: 6.92 при 100000

# Без использования «Решета Эратосфена»
def not_reshet():
    n = int(input("n="))
    arr = []
    for i in range(2, n + 1):
        # пробегаем по списку (lst) простых чисел
        for j in arr:
            if i % j == 0:
                break
        else:
            arr.append(i)
    print(arr)


def main():
    with_reshet()
    not_reshet()


cProfile.run('main()')
