
def DEL(n, m):
    return not(n % m)

for A in range(1, 13):
    correctA = 1
    for x in range(1, 1000):
        F = (not(DEL(x, A))) <= (DEL(x, 6) <= (not DEL(x, 4)))
        if F == 0:
            correctA = 0
            break
    if correctA:
        print(A) # выводит все А
