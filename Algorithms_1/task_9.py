# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

x1 = int(input('Введите первое число: '))
x2 = int(input('Введите второе число: '))
x3 = int(input('Введите третье число: '))


if (x1 < x2 < x3) | (x3 < x2 < x1):
    print(f'Среднее число {x2}')

elif (x2 < x1 < x3) | (x3 < x1 < x2):
    print(f'Среднее число {x1}')

elif (x1 < x3 < x2) | (x2 < x3 < x1):
    print(f'Среднее число {x3}')


