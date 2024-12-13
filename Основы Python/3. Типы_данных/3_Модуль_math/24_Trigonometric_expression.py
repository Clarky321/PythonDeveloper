"""
Напишите программу, вычисляющую значение тригонометрического выражения

six x + cos x + tan^2x

по заданному числу градусов x.
"""

from math import *

x = float(input())

r = (x * pi) / 180

print(sin(r) + cos(r) + tan(r) ** 2)
