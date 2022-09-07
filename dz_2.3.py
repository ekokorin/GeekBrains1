#  Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input("Введите число N: "))
lst = []
s = 1
sum = 0
for i in range(1, n+1):
    s = (1 + 1/i) ** i
    lst.append(s)
    sum = sum + lst[i-1]
print(sum)