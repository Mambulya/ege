def NumberOFdivisors(n):
    """
    finds number of divisors on the number n

    :param n: a number which divisors are found
    :return: number of divisors of n (counting 1 and n)
    """
    divisorsNumber = 2  # take into account the divisors like 1 and n
    d = 2  # is a divisor

    while d * d < n:
        if n % d == 0:  # is this d a real divisor?
            divisorsNumber += 2  # every divisor has their own couple
        d += 1
    if d * d == n:  # if n is a natural number squared (ex: 1, 4, 9 ...),
        # it has an additional divisor n**0.5
        divisorsNumber += 1

    return divisorsNumber

print(NumberOFdivisors(100))
