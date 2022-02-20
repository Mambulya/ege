for A in range(1, 100):
    isAcorrect = True
    for x in range(1, 1000):
        if ((x & 56 != 0) <= ((x & 48 == 0) <= (x & A != 0))) == False:
            isAcorrect = False
            break
    if isAcorrect:
        print(A)
