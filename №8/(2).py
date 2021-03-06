"""
itertiils.permutations() - функция для перестановок без повторений для отдельного СИМВОЛА, в то время как
itertiils.product() - функция для перестановок с повторениями для отдельного символа
Например, из набора "*!":
с помощью itertiils.permutations()  ->   ('!', '*'), ('*', '!')
itertiils.product()  ->  ('*', '*'), ('*', '!'), ('!', '*'), ('!', '!')



ЗАДАНИЕ:
Маша составляет шестибуквенные слова перестановкой букв слова КАПКАН. При этом она избегает слов с двумя 
подряд одинаковыми буквами. Сколько различных кодов может составить Маша?
"""


from itertools import product, permutations

k = 0

for i in set(permutations("КАПКАН", r = 6)):
    s = ''.join(i)
    if ("АА" not in s) and ("КК" not in s):
        k += 1

print(k)
