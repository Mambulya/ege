for m in range(2, 10**5):
    M = 1
    for j in range(10):
        M *= (m + j)
        if j >= 3:
            if 10**5 <= M <= 250000:
                print("{}:  min: {}    max: {}".format(M, m, m+j))
