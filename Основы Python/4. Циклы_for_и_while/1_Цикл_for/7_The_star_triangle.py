"""
На вход программе подаётся натуральное число n (n >= 2) - катет прямоугольного равнобедренного треугольника.

Напишите программу, которая выводит звёздный треугольник в соответствии с примером.
"""

n = int(input())
while 0 < n:
    for i in range(n):
        print("*", end="")
    print()
    n -= 1
