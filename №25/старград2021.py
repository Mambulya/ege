def NumberOfDivisors(n):
    d = 2
    divisorsNumber = 0
    maxD = 0

    if pow(n, 0.5) != int(pow(n, 0.5)):
        return 0

    while d * d < n:
        if n % d == 0:
            if divisorsNumber >= 2:
                return 0
            divisorsNumber += 2
            maxD = n // d

        d += 1

    if d * d == n:
        divisorsNumber += 1

    return maxD

for i in range(123456789, 223456789 + 1):
    res = NumberOfDivisors(i)
    if res:
        print("{}: {}".format(i, res))
