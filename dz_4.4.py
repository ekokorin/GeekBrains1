# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите степень k: '))
st = ''
for i in reversed(range(k + 1)):
    kx = random.randint(0, 100)
    if i == k:
        if kx == 0:
            st = str(random.randint(1, 100)) + '*x^' + str(k)
        elif kx == 1:
            st = 'x^' + str(k)
        else:
            st = str(kx) + '*x^' + str(k)
    elif i == 0:
        if kx == 0:
            st = st + ' = 0'
        else:
            st = st + str(kx) + ' = 0'
    elif i == 1:
        if kx == 0:
            st = st + str(random.randint(0, 100))
        elif kx == 1:
            st = st + ' + x + ' + str(random.randint(0, 100))
        else:
            st = st + ' + ' + str(kx) + '*x + ' + str(random.randint(0, 100))
    else:
        if kx == 0:
            st = st
        elif kx == 1:
            st = st + ' + x^' + str(i)
        else:
            st = st + ' + ' + str(kx) + '*x^' + str(i)
with open('file1.txt', 'w+') as f:
    f.write(st)
    f.close()

