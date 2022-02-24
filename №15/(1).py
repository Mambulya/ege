""" ЗАДАНИЕ: найти наименьшее А, чтобы выражение было тождественно истинно при любом целом х"""

for A in range(10, 1000):
    correctA = True
    for x in range(1, 1000):
        if (((x % A == 0) and (x % 15 != 0)) <= ((x %18 == 0) or (x % 15 == 0))) == False:
            correctA = False
            break
    if correctA:
        print(A)
        break
