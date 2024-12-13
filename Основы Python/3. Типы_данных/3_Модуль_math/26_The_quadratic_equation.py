"""
Даны три вещественных числа a, b, c.

Напишите программу, которая находит вещественные корни квадратного уравнения:

ax^2 + bx + c = 0

Если уравнение имеет два корня, то следует вывести их в порядке возрастания.
"""

from math import *

a, b, c = float(input()), float(input()), float(input())

D = b * b - 4 * a * c

if D < 0:
    print("Нет корней")
elif D == 0:
    print(-1 * b / 2 / a)
else:
    print(min((-1 * (b + sqrt(D)) / 2 / a), (-1 * (b - sqrt(D)) / 2 / a)))
    print(max((-1 * (b + sqrt(D)) / 2 / a), (-1 * (b - sqrt(D)) / 2 / a)))
