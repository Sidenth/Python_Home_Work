# Задание 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.
# Решите через рекурсию. В задании нельзя применять циклы.

import random


def guess_the_number(count, number):
    if count < 1:
        return print(f'Было загадано число -  {number}')
    else:
        given_number = int(input('Введите число: '))
        if given_number == number:
            print("Вы угадали!")
        else:
            if given_number > number:
                print("Ваше число больше загаданного ")
            elif given_number < number:
                print("Ваше число меньше загаданного ")
            print(f"У вас осталось {count - 1} попыток ")
            return guess_the_number(count - 1, number)


numb = random.randint(0, 100)
counter = 10
guess_the_number(counter, numb)
