n = int(input('Введите номер четверти от 1 до 4: '))
if n == 1:
    print('X > 0, Y > 0')
elif n == 2:
    print('X < 0, Y > 0')
elif n == 3:
    print('X < 0, Y < 0')
else:
    print('X > 0, Y < 0')
