
def Min7(n):
    d = 2
    minD = 100000000000

    while d * d <= n:
        if n % d == 0:
            if (d % 10 == 7) and (d != 7):
                return d
            elif ((n // d) % 10 == 7) and ((n // d) != 7):
                minD = min(minD, (n // d))
        d += 1

    return minD if minD != 100000000000 else 0

limit = 0

for i in range(800000, 1000000):
    if limit == 5:
        break
    res = Min7(i)
    if res:
        print("{}: {}".format(i, res))
        limit += 1
