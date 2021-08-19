# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

index_list = [random.randint(-10000, 10000) for _ in range(1, 10)]
print(index_list)
arr = []

for item in index_list:
    if min(index_list) < item < max(index_list):
        arr.append(item)

average = sum(arr) / len(arr)
print(f'Среднее значение: {average}')

