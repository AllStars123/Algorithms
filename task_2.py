# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = int(input('Введи натуральное число: '))
even = []
odd = []

while number > 0:
    m1 = number % 10
    if m1 % 2 == 0:
        even.append(m1)
    else:
        odd.append(m1)
    number = number // 10
print(len(even), 'Чётных цифры: ', *even)
print(len(odd), 'Нечетных цифры: ', *odd)


