"""
Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.
"""

n, n2, n3 = int(input()), int(input()), int(input())
d = 0
if n > 0 and n2 > 0 and n3 > 0:
    print(n + n2 + n3)
if n > 0 and n2 > 0 and n3 < 0:
    print(n + n2)
if n > 0 and n3 > 0 and n2 < 0:
    print(n + n3)
if n2 > 0 and n3 > 0 and n < 0:
    print(n2 + n3)
if n > 0 and n2 < 0 and n3 < 0:
    print(n)
if n2 > 0 and n < 0 and n3 < 0:
    print(n2)
if n3 > 0 and n < 0 and n2 < 0:
    print(n3)
if n3 < 0 and n2 < 0 and n < 0:
    print(0)
