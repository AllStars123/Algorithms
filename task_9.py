# Найти максимальный элемент среди минимальных элементов столбцов матрицы

rows, columns = int(input('Введи количество строк: ')), int(input('Введи количество столбцов: '))

matrix = []
min_in_rows = []

for i in range(rows):
    print(f'{i + 1}-я строка')
    arr = []
    for j in range(columns):
        arr.append(int(input()))
    matrix.append(arr)
    min_in_rows.append(min(arr))

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=' ')
    print()

print(f'Максимально число из минимальных: {max(min_in_rows)}')
