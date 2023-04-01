# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем
# слова. Будем считать, что на вход подается только одно слово, которое
# содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук
#     12
eng_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

one_point_eng = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
two_point_eng = ['D', 'G']
three_point_eng = ['B', 'C', 'M', 'P']
four_point_eng = ['F', 'H', 'V', 'W', 'Y']
five_point_eng = ['K']
eight_point_eng = ['J', 'X']
ten_point_eng = ['Q', 'Z']

rus_dict = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С',' Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

one_point_rus = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
two_point_rus = ['Д', 'К', 'Л', 'М', 'П', 'У']
three_point_rus = ['Б', 'Г', 'Ё', 'Ь', 'Я']
four_point_rus = ['Й', 'Ы']
five_point_rus = ['Ж', 'З', 'Х', 'Ц', 'Ч']
eight_point_rus = ['Ш', 'Э', 'Ю']
ten_point_rus = ['Ф', 'Щ', 'Ъ']

word = input('Введите слово: ').upper()
word_list = []
for i in word:
    word_list.append(i)
count = 0
if i in eng_dict:
	for i in range(len(word_list)):
		if word_list[i] in one_point_eng:
			count+=1
		if word_list[i] in two_point_eng:
			count+=2
		if word_list[i] in three_point_eng:
			count+=3
		if word_list[i] in four_point_eng:
			count+=4
		if word_list[i] in five_point_eng:
			count+=5
		if word_list[i] in eight_point_eng:
			count+=8
		if word_list[i] in ten_point_eng:
			count+=10
		i+=1
	print(count)
elif i in rus_dict:
	for i in range(len(word_list)):
		if word_list[i] in one_point_rus:
			count+=1
		if word_list[i] in two_point_rus:
			count+=2
		if word_list[i] in three_point_rus:
			count+=3
		if word_list[i] in four_point_rus:
			count+=4
		if word_list[i] in five_point_rus:
			count+=5
		if word_list[i] in eight_point_rus:
			count+=8
		if word_list[i] in ten_point_rus:
			count+=10
		i+=1
	print(count)
else:
	print('Ошибка ввода ')
