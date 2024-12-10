"""
Напишите программу, которая определяет наименьшее из четырёх чисел.
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a < b:
    min = a
else:
    min = b

if c < d:
    min2 = c
else:
    min2 = d

if min < min2:
    print(min)
else:
    print(min2)
