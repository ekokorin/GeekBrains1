# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на
# указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random

n = int(input('Введите N: '))
lst=[]
for i in range(n):
    lst.append(random.randint(-n, n))
print(lst)
comp = 1
with open('file.txt', 'r') as f:
    for i in f.read().split('\n'):
        comp = comp * lst[int(i)]
print(comp)
