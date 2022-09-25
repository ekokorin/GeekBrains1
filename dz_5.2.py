# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний
# ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

# Игра друг против друга

# import random
#
#
# def count(player):
#     print(player, 'Введите количество конфет которое хотите взять(не больше 28)')
#     k = int(input())
#     while k > 28:
#         print('Вы ввели количество конфет больше 28, введите 28 или меньше ')
#         k = int(input())
#     return k
#
#
# k = 2021
# player = [input('Введите имя первого игрока: '), input('Введите имя второго игрока: ')]
# i = random.randint(0, 1)
# print('Первый ходит', player[i])
# flag = i
#
# while k > 28:
#
#     k = k - count(player[flag])
#     print('На столе осталось ', k, ' конфет')
#     if flag == 0:
#         flag = 1
#     else:
#         flag = 0
#     if k = 1:
#         if flag == 0:
#             flag = 1
#         else:
#             flag = 0
#
# print('Игрок ', player[flag], ' проиграл')

# Игра человека против глупого бота

# import random
#
#
# def count(player):
#     print(player, 'Введите количество конфет которое хотите взять(не больше 28)')
#     k = int(input())
#     while k > 28:
#         print('Вы ввели количество конфет больше 28, введите 28 или меньше ')
#         k = int(input())
#     return k
#
#
# k = 2021
# player = [input('Введите имя игрока: '), 'Бот']
# i = random.randint(0, 1)
# print('Первый ходит', player[i])
# flag = i
#
# while k > 28:
#     if flag == 0:
#         k = k - count(player[flag])
#     else:
#         s = random.randint(1, 28)
#         print('Бот взял', s, 'конфет' )
#         k = k - s
#     print('На столе осталось ', k, ' конфет')
#     if flag == 0:
#         flag = 1
#     else:
#         flag = 0
#     if k = 1:
#         if flag == 0:
#             flag = 1
#         else:
#             flag = 0
#
# print('Игрок', player[flag], 'проиграл')

# Игра человека против умного бота

import random


def count(player):
    print(player, 'Введите количество конфет которое хотите взять(не больше 28)')
    k = int(input())
    while k > 28 and k != 0:
        print('Вы ввели количество конфет больше 28, введите 28 или меньше ')
        k = int(input())
    return k


def bot(lastk, u,
        z):  # lastk - пооследнее число конфет взятое игроком, u - оставшееся количество, z - флаг первого хода
    if z == 1:
        return 5
    if u <= 28:
        return u - 1
    else:
        if lastk == 28:
            return 28
        else:
            return 28 - lastk


k = 2021
player = [input('Введите имя игрока: '), 'Бот']
i = random.randint(0, 1)
print('Первый ходит', player[i])
flag = i

z = 1
n = 0
while k > 28:
    if flag == 0:
        n = count(player[flag])
        k = k - n
    else:
        s = bot(n, k, z)
        print('Бот взял', s, 'конфет')
        k = k - int(s)
    print('На столе осталось ', k, ' конфет')
    if flag == 0:
        flag = 1
    else:
        flag = 0
    if k == 1:
        if flag == 0:
            flag = 1
        else:
            flag = 0
    z = 0

print('Игрок', player[flag], 'проиграл')
