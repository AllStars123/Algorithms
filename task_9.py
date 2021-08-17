# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр

entered_list = input('Введите последовательность чисел: ').split()

max_sum = 0
right_number = 0

for item in entered_list:
    sum_1 = sum(map(int, item))
    if sum_1 > max_sum:
        max_sum = sum_1
        right_number = item
print(f'Число: {right_number} \nСумма цифр: {max}')
