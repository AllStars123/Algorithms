# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.


columns = 5
rows = 4
matrix = []
sum_row = 0

for i in range(rows):
    print(f'{i + 1}-я строка')
    arr = []
    for j in range(columns - 1):
        n = int(input())
        arr.append(n)
        sum_row += n
    arr.append(sum_row)
    matrix.append(arr)

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=' ')
    print()
