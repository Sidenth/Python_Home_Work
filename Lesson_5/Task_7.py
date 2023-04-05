# Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
# натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n - любое натуральное число.
# Пример:
# для n = 5
# 1+2+3+4+5 = 5(5+1)/2
# Нужно написать рекурсивную ф-цию только для левой части выражения!
# Результат нужно сверить с правой частью.
# Правой части выражения в рекурсивной ф-ции быть не должно!
# Решите через рекурсию. В задании нельзя применять циклы.


def is_right(number, count, new_number):
    if count >= number:
        if new_number == number * (number + 1) / 2:
            return print('Выражение верно ')
        else:
            return print('Выражение неверно ')
    else:
        new_number += number - count
        return is_right(number, count + 1, new_number)


try:
    new_number = int(input("Введите целое число: "))
    num_2 = 0
    counter = 0
    is_right(new_number, counter, num_2)
except ValueError:
    print("Ошибка ввода ")
