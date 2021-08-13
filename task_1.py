# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input('Введите трехзначное число: '))
c = []

if 100 < number < 999:
    while number > 0:
        b = number % 10
        c.append(b)
        number = number // 10
    print(sum(c))
else:
    print('Вы ввели не трёхзначное число')
