"""
Дан порядковый номер месяца (1, 2, ..., 12).
Напишите программу, которая выводит на экран количество дней в этом месяце.
Принять, что год является невисокосным.
"""

a = int(input())

if (a == 1) or (a == 3) or (a == 5) or (a == 7) or (a == 8) or (a == 10) or (a == 12):
    print(31)
elif (a == 4) or (a == 6) or (a == 9) or (a == 11):
    print(30)
elif a == 2:
    print(28)
