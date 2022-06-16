
for i in range(153222, 153271):
    a, b = 0, 0
    pares = 0

    for b in range(1, int((i // 2)**0.5) + 1):
        if pares > 1:
            break
        a2 = i - b ** 2
        if a2 <= 0:
            break

        if a2**0.5 == int(a2**0.5):
            A = min(b, int(a2**0.5))
            B = max(b, int(a2**0.5))
            pares += 1

    if pares == 1:
        print("--- {} = {}**2 + {}**2".format(i, A, B))
