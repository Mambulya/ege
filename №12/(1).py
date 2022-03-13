string = '>' + '2'*10 + '4'*11 + '7'*12

while (">2" in string) or (">4" in string) or (">7" in string):
    if ">2" in string:
        string = string.replace(">2", "72>", 1 )
    if ">4" in string:
         string = string.replace(">4", "4>22", 1 )
    if ">7" in string:
         string = string.replace(">7", "24>2", 1 )

print(string)

summa = 0

for n in string:
    if n.isdigit():
        summa += int(n)
print(summa)
