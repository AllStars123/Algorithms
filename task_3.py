# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

# a = [1, 2, 3, 4]
# b = a[::-1]
# print(''.join(map(str, b)))

number = int(input('Введите число: '))
revers = []
while number > 0:
    v1 = number % 10
    revers.append(v1)
    number = number // 10

print('Обратное: ', ''.join(map(str, revers)))
