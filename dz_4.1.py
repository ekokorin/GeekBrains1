# Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

d = input('Введите d = ')
x = input('Введите число х = ')
a = len(d[2:])  # Количество символов после точки у числа d
for i in range(len(x)):  # Находим положение точки у x
    if x[i] == '.':
        break
y = len(x[i + 1:])  # Количество символов после точки у числа x

if a < y:
    print(x[:-(y-a)])
elif a == y:
    print(x)
else:
    print(x + '0' * (a - y))
