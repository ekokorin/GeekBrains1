# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11
# print(sum([int(i) for i in input() if i != '.']))
n = input('Введите вещественное число: ')
sum = 0
for i in range(len(n)):
    if n[i].isdigit():
        sum = sum + int(n[i])
print(sum)
