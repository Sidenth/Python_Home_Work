# Задание 3.
# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.
# Пример:
# Введите число n: 3
# n + nn + nnn = 369
# given_digit = int(input("Введите целое положительное число: "))
# sum_digits = str(given_digit) + str(given_digit + given_digit) + str(given_digit + given_digit + given_digit)
# print(sum_digits)
n = input("Введите число: ")
print(f'Результат: {int(n) + int(n+n) + int(n+n+n)} ')