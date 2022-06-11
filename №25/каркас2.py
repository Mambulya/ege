def NumberOFdivisors(n):
    """
    finds number of divisors on the number n

    :param n: a number which divisors are found
    :return: list: number of divisors of n (counting 1 and n), every divisor
    """
    divisorsNumber = 2  # take into account the divisors like 1 and n
    d = 2  # is a divisor
    allDivisors = [1, n]

    while d * d < n:
        if n % d == 0:  # is this d a real divisor?
            divisorsNumber += 2  # every divisor has their own couple
            allDivisors.append(d)
            allDivisors.append(n // d)
        d += 1

    if d * d == n:  # if n is a natural number squared (ex: 1, 4, 9 ...),
        # it has an additional divisor n**0.5
        divisorsNumber += 1
        allDivisors.append(d)

    return [divisorsNumber] + sorted(allDivisors)

for n in range(174457, 174506):
    res = NumberOFdivisors(n)
    if res[0] == 4:
        print("{}: {} {}".format(n, res[2], res[3]))
        
# так как числа идут по возрастанию, то и их делители тоже в произведении идут по возрастанию
