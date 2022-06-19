def isPrime(n):
    d = 2

    while d * d <= n:
        if n % d == 0:
            return False
        d += 1

    return True

def F(n, oldd):
    """ смотрит, можно ли разложить первый делитель d(=n) на 2 различных
        делятеля, отличных от старого делителя oldd
    """
    d = 2

    while d * d < n:
        if n % d == 0:
            if (d != oldd) and ((n // d) != oldd):
                return True
        d += 1

    return False

def Divisors(n):
    d = 2

    while d * d < n:
        if n % d == 0:
            #if isPrime(d) and isPrime(n//d):
                #return True
            if F(n//d, d):
                return False
        d += 1

    return True


limit = 0
print("let's go")
for k in range(1, 100):
    if limit == 5:
        break
    M = 7000000 + k
    if Divisors(M):
        print(k)
        limit += 1
