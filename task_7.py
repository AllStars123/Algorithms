# Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


number = int(input())
natural_number_1 = 0

for _ in range(1, number + 1):
    natural_number_1 += _

natural_number_2 = number * (number + 1) // 2
print(natural_number_1)
print(natural_number_2)
