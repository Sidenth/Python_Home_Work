# Задача 30:  Заполните массив элементами арифметической прогрессии. Её
# первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
first_element = int(input("Введите первый элемент прогрессии: "))
difference = int(input("Введите разность прогрессии: "))
amount_of_elements = int(input("Введите количество элементов: "))
arithmetic_progression = []
for i in range(amount_of_elements):
    arithmetic_progression.append(first_element + (i - 1) * difference)
print(arithmetic_progression)
