"""
Назовём число интересным, если в нём разность максимальной и минимальной цифры равняется средней по величине цифре.
Напишите программу, которая определяет, интересное число или нет.
Если число интересное, следует вывести текст «Число интересное» (без кавычек), иначе – «Число неинтересное» (без кавычек).
"""

n = int(input())
n1 = n % 10
n2 = n % 100 // 10
n3 = n // 100
if (max(n1, n2, n3) - min(n1, n2, n3)) == (
    n1 + n2 + n3 - max(n1, n2, n3) - min(n1, n2, n3)
):
    print("Число интересное")
else:
    print("Число неинтересное")
