"""
Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
"""

s1, s2, s3 = input(), input(), input()
n1, n2, n3 = len(s1), len(s2), len(s3)

if min(n1, n2, n3) == n1:
    print(s1)
elif min(n1, n2, n3) == n2:
    print(s2)
else:
    print(s3)

if max(n1, n2, n3) == n1:
    print(s1)
elif max(n1, n2, n3) == n2:
    print(s2)
else:
    print(s3)
