def NumberOFdivisors(n):
    """
    finds number of divisors on the number n

    :param n: a number which divisors are found
    :return: list: number of divisors of n (counting 1 and n), every divisor
    """
    if pow(n, 0.5) != int(pow(n, 0.5)): # НЕЧЁТНОЕ КОЛИЧЕСТВО ДЕЛИТЕЛЕЙ МОЖЕТ БЫТЬ ЛИШЬ У НАТУРАЛЬНЫХ КВАДРАТОВ! из-за доп делителя (строчка 24)
        return [0]

    divisorsNumber = 2  # take into account the divisors like 1 and n
    d = 2  # is a divisor
    allDivisors = [1, n]

    while d * d < n:
        if n % d == 0:  # is this d a real divisor?
            divisorsNumber += 2  # every divisor has their own couple
            if divisorsNumber > 5:   # ТАК КАК ДЕЛИТЕЛЯ ВСЕГО 3 (уникальных), ТО НЕТ СМЫСЛА РАССМАТРИВАТЬ ЧИСЛА, У КОТОРЫХ ИХ БОЛЬШЕ
                # 5 - это вместе с 1 и самим числом
                break
            allDivisors.append(d)
            allDivisors.append(n // d)
        d += 1

    if d * d == n:  # if n is a natural number squared (ex: 1, 4, 9 ...),
        # it has an additional divisor n**0.5
        divisorsNumber += 1
        allDivisors.append(d)

    return [divisorsNumber] + sorted(allDivisors)

for n in range(4234679, 10157813):
    res = NumberOFdivisors(n)
    if res[0] == 5:
        print("{}: {}".format(n, res))
