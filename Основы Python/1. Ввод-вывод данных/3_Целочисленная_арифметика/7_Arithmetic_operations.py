"""
Напишите программу, которая принимает на вход два числа a и b, вычисляет сумму, разность и произведение для этих чисел и выводит текст в следующем формате:

<число a> + <число b> = <сумма чисел a и b>
<число a> - <число b> = <разность чисел a и b>
<число a> * <число b> = <произведение чисел a и b>
"""

a = int(input())
b = int(input())
print(a, "+", b, "=", a + b)
print(a, "-", b, "=", a - b)
print(a, "*", b, "=", a * b)
