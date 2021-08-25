# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


# Способ 1
from collections import deque, defaultdict

first = input('Введите первое число: ')
second = input('Введите второе число: ')

first = int(first, 16)
second = int(second, 16)

sum_num = first + second
mul_num = first * second

print(f'Сумма чисел: {hex(sum_num)}')
print(f'Произведение чисел: {hex(mul_num)}')


# Способ 2

def in_decimal(inp):
    num = deque(inp)
    num.reverse()
    decimal = 0
    for item in range(len(num)):
        decimal += table[num[item]] * 16 ** item
    return decimal


def custom_hex(num_1):
    num = deque()
    while num_1 > 0:
        a = num_1 % 16
        for item in table:
            if table[item] == a:
                num.append(item)
        num_1 //= 16
    num.reverse()
    return list(num)


list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
table = defaultdict(int)
counter = 0
for key in list_of_numbers:
    table[key] += counter
    counter += 1
print(table)

num_1 = in_decimal(input('Введите первое число: ').upper())
num_2 = in_decimal(input('Введите второе число: ').upper())

print(f'Сумма чисел: {custom_hex(num_1 + num_2)}')
print(f'Произведение чисел: {custom_hex(num_1 * num_2)}')
