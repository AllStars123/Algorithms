# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

index_list = [random.randint(1, 1000) for _ in range(1, 20)]
print(index_list)
min_num, max_num = min(index_list), max(index_list)
min_ind, max_ind = index_list.index(min_num), index_list.index(max_num)
index_list[min_ind], index_list[max_ind] = max_num, min_num
print(index_list)
