"""
Напишите программу, которая по введённым целым значениям a и b вычисляет значение следующего выражения:

3(a + b)^3 + 275b^2 - 127a - 41
"""

a = int(input())
b = int(input())
v = (a + b) * (a + b) * (a + b)
c = b * b
print(3 * (v) + 275 * c - 127 * a - 41)
