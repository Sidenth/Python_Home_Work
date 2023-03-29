# Задание 2.
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# given_time = 10000;
# seconds = given_time % (24*3600);
# hours = seconds / 3600;
# seconds = seconds % 3600;
# minutes = seconds / 60;
# seconds = seconds % 60;
# # print(f'{hours}:{minutes}:{seconds}');
# print(float("{0:.1f}".format(hours)));
import datetime
given_time = int(input("Введите время в секундах: "));
formated_time = str(datetime.timedelta(seconds = given_time));
print(formated_time);
