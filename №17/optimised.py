
with open("E:/ЕГЭ/ИНФОРМАТИКА/фипи ВСЕ ВАРИАНТЫ/17/17var2.txt") as f:
    a = int(f.readline())
    MinSum = 20000
    couples = 0

    for line in f:
        b = int(line)
        if (a > 0 and (pow(a, 0.5) == int(pow(a, 0.5)))) or (b > 0 and (pow(b, 0.5) == int(pow(b, 0.5)))):
            couples += 1
            MinSum = min(MinSum, a + b)
            print("a: {}  b: {}  Minsum: {}".format(a, b, MinSum))
        a = b

    print(couples, MinSum)

    
    
