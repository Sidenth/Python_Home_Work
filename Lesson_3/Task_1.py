# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.
# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень

# season_list = ['зима', 'весна', 'лето', 'осень']
# given_season = int(input('Введите номер месяца: '))
# if given_season>=1 and given_season<=3:
#     print(f"{season_list[0]} ")
# elif given_season>=4 and given_season<=6:
#     print(f"{season_list[1]} ")
# elif given_season>=7 and given_season<=9:
#     print(f"{season_list[2]} ")
# elif given_season>=10 and given_season<=12:
#     print(f"{season_list[3]} ")
# else:
#     print("Ошибка ввода")

s ={}
for i in range(1,3):
    s[i]='зима'
for i in range(3,6):
    s[i]='весна'
for i in range(6,9):
    s[i]='лето'
for i in range(9,12):
    s[i]='осень'
s[12] = 'зима'
season_number = int(input('Введите номер месяца: '))
if season_number>0 and season_number<13:
    print(s[season_number])
else:
    print('Ошибка')

