def task23(p, N):
    """
    :param p: the first number
    :param N: the last number
    :return: number of variations how to reach n from p
    """
    operations = [0] * (N-p + 1)
    operations[0] = 1
    for t in range(1, N - p + 1):
        if t != 15:
            operations[t] += operations[t-1]
        if t >= 2:
            operations[t] += operations[t-2]

    Ts = ['T' + str(n) for n in range(3, N+1)]
    print("           ", end='')
    print(*Ts)
    print(
    """
    list: {}
    answer - {}
    """.format(operations, operations[-1]))

task23(3, 18)