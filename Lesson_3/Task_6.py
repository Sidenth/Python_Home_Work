# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

N = int(input("Введите количество элементов массива: "))
X = int(input('Введите число X: '))
current_list = []
for i in range(1, N + 1):
    current_list.append(i)
    i += 1
print(current_list)
count = 0
min = X - current_list[0]
index = 0
if X in current_list:
    min = X
elif X < 0:
    print('Ошибка ввода ')
else:
    for i in range(len(current_list)):
        if X - current_list[i] < min:
            min = X - current_list[i]
            index = i
            i += 1
    min = current_list[index]
print(f"Ближайший по значению элемент - {min}")
