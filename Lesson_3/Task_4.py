# 4. Реализовать функцию my_func(), которая принимает три позиционных
# аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:
# 1) используя функцию sort()
# 2) без функции sort()


# def my_func(list_2):
#     list_2.sort()
#     print(list_2[1]+list_2[2])
# list_2 = []
# for i in range(1,4):
#     list_2.append(int(input(f"Введите {i}-е число ")))
# if list_2[0]==list_2[1]==list_2[2]:
#     print('Все числа равны ')
# else:
#     my_func(list_2)
def my_func(list_1):
    max = list_1[0]
    if max < list_1[1] or max < list_1[2]:
        max = list_1[1]
        if max < list_1[2]:
            max = list_1[2]
    list_1.remove(max)
    max_2 = list_1[0]
    if max_2 < list_1[1]:
        max_2 = list_1[1]
    print(max + max_2)


list_1 = []
for i in range(1, 4):
    list_1.append(int(input(f"Введите {i}-е число ")))
if list_1[0] == list_1[1] == list_1[2]:
    print('Все числа равны ')
else:
    my_func(list_1)
