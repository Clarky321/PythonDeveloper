"""
n школьников делят k мандаринов поровну, неделящийся остаток остается в корзине.
Сколько целых мандаринов достанется каждому школьнику?
Сколько целых мандаринов останется в корзине?
"""

kinder = int(input())
mandarins = int(input())
num1 = mandarins // kinder
num2 = mandarins % kinder
print(num1)
print(num2)