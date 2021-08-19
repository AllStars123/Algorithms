# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random


index_list = [random.randint(-10000, 10000) for _ in range(1, 10)]
print(index_list)
arr = []
for item in index_list:
    if item < 0:
        arr.append(item)
print(f'Максимальный отрицательный элемент в массиве: {max(arr)} его позиция в массиве {index_list.index(max(arr))}')
