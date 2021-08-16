# для нахождения наибольшего общего делителя (НОД) пары целых чисел

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(5, 8))
