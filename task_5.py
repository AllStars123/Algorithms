# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

x1 = ord(input('Введите первую границу числа: '))
x2 = ord(input('Введите вторую границу числа: '))

print(f'Место в алфавите первого значения: {x1 - 96}\n', f'Место в алфавите первого значения: {x2 - 96}', )

print(f'Между ними находится {x2 - x1} букв')