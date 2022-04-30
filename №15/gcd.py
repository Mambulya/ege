"""
ВЗПР(a, b) - утверждение "числа a и b - взаимнопростые"
"""

from math import gcd

def ВЗПР(a, b):
    return 1 if gcd(a, b) == 1 else 0
