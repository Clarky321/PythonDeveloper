"""
В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом.
Напишите программу, которая определяет номер купе, в котором находится место с заданным номером (нумерация мест сквозная, начинается с 1).
"""

n = int(input())
m = 4
k = (n + m - 1) // m
print(k)
