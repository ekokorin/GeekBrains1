x = float(input('Введите X: '))
y = float(input('Введите Y: '))

if x and y > 0:
    print('Точка в 1 четверти системы координат')
elif x > 0 and y < 0:
    print('Точка во 2 четверти системы координат')
elif x and y < 0:
    print('Точка в 3 четверти системы координат')
elif x < 0 and y > 0:
    print('Точка в 4 четверти системы координат')
elif x == 0 and y != 0:
    print('Точка на оси Y системы координат')
elif x != 0 and y == 0:
    print('Точка на оси X системы координат')
else:
    print('Точка в начале системы координат')
