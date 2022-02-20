"""
task:
Текстовый файл состоит не более чем из 106 заглавных латинских букв. Определите символ,
который чаще всего встречается в файле сразу после буквы X. В ответе запишите сначала этот
символ, а потом сразу (без разделителя) сколько раз он встретился после буквы X. Например, в
тексте XBCXXBXDDD после буквы X два раза стоит B, по одному разу – X и D. Для этого текста
ответом будет B2.
"""

with open("C:/Users/admin/Downloads/for24.txt") as f:
    string = f.readline()
    letters = [0] * 26

    for i in range(1, len(string)):
        if string[i-1] == "X":
            letters[ord(string[i]) - 65] += 1

    maxL = sorted(letters)[-1]
    print("{}{}".format(chr(letters.index(maxL) + 65), maxL))
