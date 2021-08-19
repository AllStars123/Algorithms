# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться
import random

index_list = [random.randint(-10000, 10000) for _ in range(1, 10)]
print(index_list)

min_1 = index_list.pop(index_list.index(min(index_list)))
min_2 = min(index_list)

print(f'Наименьшие числа: {min_1}, {min_2}')

