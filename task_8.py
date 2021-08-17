# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

entered_list = input('Введите последовательность чисел: ').split()
search_number = int(input('Какую цифру нужно посчитать: '))

num_list = list(map(int, entered_list))

counter = 0
for item in num_list:
    if item == search_number:
        counter += 1
print(f'В веденной последовательности число {search_number} найдено {counter} раз')
