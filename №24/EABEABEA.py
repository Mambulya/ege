"""
task:
(А.М. Кабанов) В текстовом файле находится цепочка из символов латинского алфавита A, B,
C, D, E. Найдите максимальную длину цепочки вида EABEABEABE... (составленной из фрагментов
EAB, последний фрагмент может быть неполным).

doc: XEAEABXEABEABEABEA
"""

with open("C:/Users/admin/Downloads/for24.txt") as f:
    string = f.readline()
    answer = 0
    maxAnswer = 0
    for i in range(len(string)):
        if any((answer % 3 == 0 and string[i] == 'E', answer % 3 == 1 and string[i] == 'A',
                answer % 3 == 2 and string[i] == 'B')):
            answer += 1
            if answer >= 3:
                maxAnswer = max(maxAnswer, answer)
                
            # logging   
            print("{}, answer - {}, maxAnser - {}".format(string[i], answer, maxAnswer))

        else:
            answer = 0
print(maxAnswer)
