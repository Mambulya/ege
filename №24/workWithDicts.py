"""
ЗАДАНИЕ:
24. Текстовый файл состоит не более чем из 10^6 символов А, B, C и D. 
Определите, какой символ чаще всего стоит перед последовательно стью символов «AD». 
Если несколько символов встречаются одинако вое число раз, то в ответе запишите тот, который стоит позже в алфавите. 
В ответе запишите без пробелов этот символ и сколько раз он стоит перед последовательностью «AD». Например, в25. 
Для выполнения этого задания следует написать программу.
"""

with open("...") as File:
    mainLetter = ''
    mainCount = -1
    letters = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    text = File.readline()

    for i in range(1, len(text) - 1):
        if text[i] == 'A':
            if text[i+1] == 'D':
                letters[(text[i-1])] += 1

    for key in letters:
        if letters[key] >= mainCount:
            mainCount = letters[key]
            mainLetter = key
    print(mainLetter, mainCount)
