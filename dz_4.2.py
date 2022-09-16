# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

from sympy import *

n = int(input('Введите число N = '))
lst = []


# def isprime(k):     # Проверяем число простое или нет
#     if k == 2 or k == 3: return True
#     if k % 2 == 0 or k < 2: return False
#     for i in range(3, int(k ** 0.5) + 1, 2):
#         if k % i == 0:
#             return False
#     return True

for i in range(1, n + 1):
    if n % i == 0 and isprime(i):  # Если число делится на цело и простое то добавляем в список
        lst.append(i)
print(lst)
