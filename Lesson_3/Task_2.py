# 2. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль (try except).
# Пример:
# Введите первое число: 10
# Введите второе число: 0
# Вы что? Пытаетесь делить на 0!
# Process finished with exit code 0
# Пример:
# Введите первое число: 10
# Введите второе число: 10
# 1.0
# Process finished with exit code 0
def division_of_two(numb_1, numb_2):
    try:
        print(numb_1 / numb_2)
    except ZeroDivisionError:
        print('Вы что? Пытаетесь делить на 0!')


number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
division_of_two(number_1, number_2)
