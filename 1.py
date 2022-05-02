def F(n, t):
    """
    
    :param n: start number
    :param t: aim number
    :return: number of programs variations
    """

    operations = [0]*n + [1] + [0] * (t - n)

    for i in range(n+1, len(operations)):
        operations[i] += operations[i - 1]
        if (i <= 10 or i == 20) and not (i % 2):
            operations[i] += operations[i // 2]
        if not(i % 5) and (i == 5 or i == 10):
            operations[i] += operations[i // 5]
        print(i, operations[i])
    print(operations)
    return operations[-1]




print(F(1, 38))
