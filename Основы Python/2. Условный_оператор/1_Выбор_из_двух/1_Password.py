"""
При регистрации на сайтах требуется вводить пароль дважды.
Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля.

Напишите программу, которая сравнивает пароль и его подтверждение.
Если они совпадают, то программа выводит текст «Пароль принят» (без кавычек), иначе  «Пароль не принят» (без кавычек).
"""

password_1 = str(input())
password_2 = str(input())

if password_1 == password_2:
    print("Пароль принят")
else:
    print("Пароль не принят")

