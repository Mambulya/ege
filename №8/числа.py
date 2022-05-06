from itertools import permutations

"""
ЗАДАНИЕ:
(ЕГЭ-2020) Сколько существует шестизначных чисел, делящихся на 5, в которых каждая цифра
может встречаться только один раз, при этом никакие две чётные и две нечётные цифры не стоят рядом.
"""

k = 0

for i in permutations("1234567890", r = 6):
    s = "".join(i)
    if (s[-1] == '5' or s[-1] == '0') and (s[0] != '0'):

        d1 = int(s[0]) % 2
        d2 = int(s[1]) % 2
        d3 = int(s[2]) % 2
        d4 = int(s[3]) % 2
        d5 = int(s[4]) % 2
        d6 = int(s[5]) % 2

        l = [d1 + d2, d2 + d3, d3 + d4, d4 + d5, d5 + d6]

        if (0 not in l) and (2 not in l):
            k += 1

print(k)
