# Найдите сумму цифр трехзначного числа.
# *Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
given_number =int(input("Введите трехзначное число: "))
result = given_number%10 + (given_number//10)%10 + given_number//100
print(result)