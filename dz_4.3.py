# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности.

lst_new = []

lst = [int(i) for i in input('Введите список чисел через пробел: ').split()]
print(lst)

for i in range(len(lst)):
    if lst.count(lst[i]) == 1:
        lst_new.append(lst[i])
print(lst_new)
