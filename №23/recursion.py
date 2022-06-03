"""
x: start number
y: aim number
return: amount of operations
"""
def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x + 1, y) + f(x * 4, y)


print(f(1, 32))
