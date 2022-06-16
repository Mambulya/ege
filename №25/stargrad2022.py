
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

    while d * d < n:
        if n % d == 0:
            if (d != oldd) and ((n // d) != oldd):
                return 1
        d += 1

    return 0


def divisors3(n):
    """ рассматривает пары делителей числа n """
    d = 2

    while d * d <= n:
        if n % d == 0:
            if (not isPrime(d)):
                if F(d, n // d):
                    return n

            if (not isPrime(n // d)):
                if F(n // d, d):
                    return n
        d += 1

    return 0


limit = 0

for k in range(1, 100):
    if limit == 5:
        break
    M = 7000000 + k
    if (not divisors3(M)):
        print(k)
        limit += 1
