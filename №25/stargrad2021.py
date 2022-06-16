def NumberOfDivisors(n):
    d = 2
    allDivisors = []

    while d * d < n:
        if len(allDivisors) >= 10:
            return sorted(allDivisors)
        if n % d == 0:
            allDivisors.append(d)
            allDivisors.append(n // d)
        d += 1

    if d * d == n:
        if n % d == 0:
            allDivisors.append(d)

    if len(allDivisors) < 5:
        return 0

    return sorted(allDivisors)

limit = 0

for i in range(200000000 + 1, 10**9):
    M = 1
    if limit == 5:
        break
    res = NumberOfDivisors(i)
    if res != 0:
        for j in range(0, 5):
            M *= res[j]
        if M < i:
            print("{}: {}".format(i, M))
            limit += 1
