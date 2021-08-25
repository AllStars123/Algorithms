# Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.


rows = int(input('Введите количество предприятий: '))
columns = 4
matrix = []
average = {}
for i in range(rows):
    arr = []
    print(f'Прибыль {i + 1}-ого предприятия:  ')
    for j in range(columns):
        arr.append(int(input(f'Прибыль за {j + 1}-ый квартал: ')))

    matrix.append(arr)
    s = sum(matrix[i]) / 4
    average[f'Предприятие {i + 1}'] = s


av = 0
for items in average.values():
    av += items
av = av / rows

more = []
less = []


for k, v in average.items():
    if v > av:
        more.append(k)
    else:
        less.append(k)

print(f'Средняя прибыль всех предприятий: {av}')
print(average)
print('Больше средней прибыли:', *more)
print('Меньше средней прибыли:', *less)
