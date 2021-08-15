# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.


number = int(input('Введите количество: '))
arr = []
row = 2
for item in range(number):
    row = row / 2
    arr.append(row)

for item in arr:
    index = arr.index(item)
    if index % 2 != 0:
        arr[index] *= -1
print('Ряд: ', *arr)
print('Сумма ряда: ', sum(arr))
