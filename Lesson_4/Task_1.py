# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит
# сами элементы множеств.

def fill_list(my_list, number):
    for counter in range(number):
        my_list.append(int(input(f'Введите {counter + 1}-й элемент ')))
    return my_list


n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))
first_list = []
second_list = []
print(fill_list(first_list, n))
print(fill_list(second_list, m))
first_set = set(first_list)
second_set = set(second_list)
res_set = sorted(first_set.intersection(second_set))
print(res_set)
