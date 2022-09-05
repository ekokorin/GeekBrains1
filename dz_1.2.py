x = input('Введите X: ')
y = input('Введите Y: ')
z = input('Введите Z: ')

print(not(x or y or z) == (not x and not y and not z))