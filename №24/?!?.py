"""
ЗАДАНИЕ:
24. Текстовый файл состоит не более чем из 106 символов %, !, ?. Определите максимальную длину цепочки, состоящей из одного сим вола вида !, или %, или ?.

Для выполнения этого задания следует написать программу.
"""
with open("...") as File:
    text = File.readline()
    count = 0
    maxCount = 0
    for i in range(len(text)):
        if any((count % 3 == 0 and text[i] == '?',
                count % 3 == 1 and text[i] == '!',
                count % 3 == 2 and text[i] == '?')):
            count += 1
            if count >= 3:
                maxCount = max(maxCount, count)
        elif text[i] == '?':
            count = 1
        else:
            count = 0

    print(maxCount)
