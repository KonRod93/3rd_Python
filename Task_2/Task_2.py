# Задача 2.
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 6
# -> 5


import random
n = int(input("Введите количество элементов в массиве: "))
list = [random.randrange(0, 10) for i in range(n)]
print(*list)
value = int(input("Введите искомое число: "))


def close_value(list, value):
    x = list[0]
    for list in list:
        if abs(list - value) < abs(x - value):
            x = list
    return x


print(f"Ближайшим число к {value} является {close_value(list, value)}")