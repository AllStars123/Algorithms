# Определить, какое число в массиве встречается чаще всего.

import random

index_list = [random.randint(1, 1000) for _ in range(1, 200)]

max_count = 0
num = 0

for item in index_list:
    count_of_item = index_list.count(item)
    if max_count < count_of_item:
        max_count = count_of_item
        num = item

print(f'Число {num} встречается чаще всего - {max_count} раз')
