# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4
def sum_a_b(number_1, number_2):
    if number_2 == 0:
        return print(number_1)
    else:
        return sum_a_b(number_1 + 1, number_2 - 1)


try:
    first_number = int(input("Введите первое число: "))
    second_number = int(input("Введите второе число: "))
    sum_a_b(first_number, second_number)
except ValueError:
    print("Ошибка ввода")
