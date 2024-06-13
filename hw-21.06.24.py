import random

list1 = [random.randint(1, 100) for _ in range(10)]
list2 = [random.randint(1, 100) for _ in range(10)]

list3 = list1 + list2

list4 = list(set(list3))

list5 = [item for item in list1 if item in list2]

list6 = [item for item in list1 if item not in list2] + [item for item in list2 if item not in list1]

list7 = [min(list1), max(list1), min(list2), max(list2)]

print("Список 1:", list1)
print("Список 2:", list2)
print("Объединенный список:", list3)
print("Список без повторений:", list4)
print("Список с общими элементами:", list5)
print("Список с уникальными элементами:", list6)
print("Список с минимальным и максимальным значениями:", list7)
