def isPrime(n):
    """
    checks if the number n is prime (True/False)
    :param n: number
    :return: bool
    """
    if n == 0 or n == 1:          # zero, one are NOT prime numbers
        return False
    d = 2   # every number has at least 2 divisors (1 and n)

    while d * d <= n:
        if n % d == 0:
            return False    # if n has at least 1 additional divisor, it is not prime
        d += 1

    return True
