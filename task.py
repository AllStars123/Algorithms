# Найти максимальный элемент среди минимальных элементов столбцов матрицы
import sys

rows, columns = int(input('Введи количество строк: ')), int(input('Введи количество столбцов: '))

matrix = []
min_in_rows = []

print(sys.getrefcount(matrix))
print(sys.getsizeof(matrix))
# 56 байт - 40 на лист + 2 ссылки по 8 байт

for i in range(rows):
    print(f'{i + 1}-я строка')
    arr = []
    for j in range(columns):
        arr.append(int(input()))
    matrix.append(arr)
    min_in_rows.append(min(arr))

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=' ')
    print()

print(f'Максимально число из минимальных: {max(min_in_rows)}')
matrix = []
# 88 байт - 40 на лист + 2 ссылки по 8 байт + 32 это константная величина за элементы в листе(плата за новые элементы) именно на 64 бит системе
print(sys.getrefcount(matrix))
print(sys.getsizeof(matrix))
print(matrix)


import random
import sys

index_list = [random.randint(-10000, 10000) for _ in range(1, 26)]
print(index_list)

min_1 = index_list.pop(index_list.index(min(index_list)))
min_2 = min(index_list)

print(f'Наименьшие числа: {min_1}, {min_2}')

print(sys.getrefcount(index_list))
# 184 байта - 40 лист + 2 ссылки по 8 байт + выделятся на 16 элементов gj 8 байт, дальше будет выделтся на каждые 10 эелементов по 80 байт
print(sys.getsizeof(index_list))