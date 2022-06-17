with open("E:/ЕГЭ/ИНФОРМАТИКА/№24/1-4.txt") as f:
    string = f.readline().rstrip()
    current = 0
    maxL = 0

    for i in range(len(string) - 1):
        if string[i] == '1':
            if string[i + 1] == '2' or string[i + 1] == '3':
                maxL = max(maxL, current + 1)
                current = 0
            else:
                current += 1

        elif string[i] == '2' or string[i] == '3':
            if string[i+1] == '1':
                maxL = max(maxL, current + 1)
                current = 0
            else:
                current += 1

        else:
            current += 1
    maxL = max(maxL, current)

    print(maxL)
