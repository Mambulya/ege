def findAllPrime(n):
    """
    the function finds all prime numbers from 2 to n
    алгоритм: решето эратосфена
    :param n: the end number
    :return:  a list which consists only prime numbers
    """
    resh = [1] * n  # every index reflects its number
    resh[0], resh[1] = 0, 0  # only numbers, which >= 2, are considered

    for i in range(len(resh)):  # the same for i in range(n):
        if resh[i] == 1:    # if this number hasn't been deleted as not prime yet
            for j in range(i**2, n, i):   # every number that occurs with frequency i*times is divisible by i
                if j % i == 0:
                    resh[j] = 0
    return [i for i in range(n) if resh[i] == 1]

print(findAllPrime(20))
