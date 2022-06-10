"""
ЗАДАНИЕ:
текстовый файл состоит не более чем из 10^6 символов k  l m n o p. Определите максимальное количество 
подряд идущих одинаковых символов - таких, что до и после них в файле находятся два одинаковых других символа.
"""
with open("...") as f:

    string = f.readline().rstrip()
    maxCount = 0
    currentCount = 1
    fLetter = ''
    firestIndex = 0

    for i in range(1, len(string) - 1):

        if string[i] == string[i+1]:
            currentCount += 1
            if string[i] != string[i-1]:
                fLetter = string[i-1]
        else:
            if string[i+1] == fLetter:
                maxCount = max(maxCount, currentCount)
            fLetter = ''
            currentCount = 1

    if string[-1] == fLetter:
        maxCount = max(maxCount, currentCount)

    print(maxCount)
