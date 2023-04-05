# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def exponentiation(number_1, number_2, count, result):
    if count >= number_2:
        return print(result)
    else:
        result *= number_1
        return exponentiation(number_1, number_2, count + 1, result)


try:
    first_number = int(input("Введите первое число: "))
    second_number = int(input("Введите второе число: "))
    counter = 0
    total = 1
    exponentiation(first_number, second_number, counter, total)
except ValueError:
    print("Ошибка ввода")
