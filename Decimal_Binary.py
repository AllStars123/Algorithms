# Функция перевода десятичного числа в двоичный формат

def binary(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s


while True:
    n = int(input())
    if n != 0:
        print(binary(n))
    else:
        break
