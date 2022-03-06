"""
ЗАДАНИЕ:
Обозначим через ВЗПР(x, y) утверждение "натуральные числа х и y не имеют общих натуральных делителей, кроме 1". При каком наименьшем натуральном значении A формула
(ВЗПР(х, 360) -> ВЗПР(х, А)) /\ (ВЗПР(х, А) -> ВЗПР(х, 240)) истинна при любом натуральном х.
"""

def ВЗПР(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return 0 if (a+b) != 1 else 1


for A in range(0, 1000):
    correctA = True
    for x in range(1, 1001):
        if not ((ВЗПР(x, 360) <= ВЗПР(x, A)) and (ВЗПР(x, A) <= ВЗПР(x, 240))):
            correctA = False
            break
    if correctA:
        print(A)
        break
print("end")
