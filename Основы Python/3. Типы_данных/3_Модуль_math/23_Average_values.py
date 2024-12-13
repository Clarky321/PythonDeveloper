"""
В математике выделяют следующие средние значения:

среднее арифметическое чисел a и b: a + b / 2

среднее геометрическое чисел a и b: a * b

среднее гармоническое чисел a и b: 2ab / a + b

среднее квадратичное чисел a и b: a^2 + b^2 / 2

"""

from math import sqrt

a = float(input())
b = float(input())

print((a + b) / 2)
print(sqrt(a * b))
print((2 * a * b) / (a + b))
print((sqrt((a * a + b * b) / 2)))
