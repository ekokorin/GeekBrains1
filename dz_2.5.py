# Реализуйте алгоритм перемешивания списка.
import random

#lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lst = ['Маша', 'Вася', 'Коля', 'Петя', 'Ира', 'Наташа']
lst_new = []
while lst != []:
    rand = random.randint(0, len(lst)-1)
    lst_new.append(lst[rand])
    lst.pop(rand)
print(lst_new)