"""
ЗАДАНИЕ:
24. Текстовый файл состоит не более чем из 106 символов %, !, ?. Определите максимальную длину цепочки, состоящей из одного сим вола вида !, или %, или ?.
"""
with open("...") as File:
    text = File.readline()
    count = 1
    maxCount = 0
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count += 1
            continue
        else:
            maxCount = max(maxCount, count + 1)
            count = 0

    print(maxCount)
