
def isPrime(n):
    if n == 1 or n == 0:
        return 0

    d = 2

    while d * d <= n:
        if n % d == 0:
            return 0
        d += 1
    return 1


def F(n, oldd):
    """ определяет есть ли среди простых делителей d(=n) отличные от oldd"""
    d = 2

    while d * d < n:  # если "while d * d <= n:", то d(=n) разобъём на 1 делитель(2 равных), а нужно на 2
        if n % d == 0:
            if (d != oldd) and ((n // d) != oldd):  # можем ли первый делительразбить на 2 разных, не похожих на второй изначальный?
                if (isPrime(d)) and (isPrime(n // d)):  # итак, они подходят. Но являются ли они простыми числами?
                    return 1
        d += 1

    return 0


def divisors3(n):
    """ рассматривает пары делителей числа n """
    d = 2

    while d * d < n:    # можно и while d * d <= n: 
        if n % d == 0:    # d и (n // d) - изначальные делители числа n
            if (not isPrime(d)) and (isPrime(n // d)):  # можно ли d разбить на произведение двух чисел? При этом (n // d) должен
                if F(d, n // d):                        # оставаться простым так как в задании требуются 3 различных ПРОСТЫХ делителя
                    return n
                                                        # если не получилось с d, посмотри n // d:
            if (not isPrime(n // d)) and (isPrime(d)):  # можно ли (n // d) разбить на произведение двух чисел? При этом d должен
                if F(n // d, d):                        # оставаться простым так как в задании требуются 3 различных ПРОСТЫХ делителя
                    return n
        d += 1

    return 0

count = 0
maxI = 0

for i in range(105673, 220784 + 1):
    res = divisors3(i)
    if res:
        count += 1
        maxI = max(maxI, i)

print(count, maxI)
