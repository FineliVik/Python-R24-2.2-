from csv import reader
import random

count=0
flag = 0
tags = []
popular=[]

# Используя приложенный файл books.csv или books-en.csv, выполнить следующее:
# №1 Вывести количество записей, у которых в поле Название строка длиннее 30 символов.

with open("books.csv", "r") as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        if len(row[1]) > 30:
            count+=1
print(f'Кол-во записей, у которых в поле Название строка длиннее 30 символов = {count}')


print('\n')
# №2 Реализовать поиск книги по автору, использовать ограничение на выдачу в зависимости от варианта (От 200 рублей).

search = input('Введите поисковой запрос: ')

with open("books.csv", "r") as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        lower_case = row[4].lower()
        index = lower_case.find(search.lower())
        if (index != -1) and (float(row[7]) > 200):
            print(row[1])
            flag+=1
    if flag == 0:
        print('Ничего не найдено')
    else:
        pass
print('\n')

# №3 Реализовать генератор библиографических ссылок вида <автор>. <название> - <год> для 20 записей.
# Записи выбрать произвольно. Список сохраняется как отдельный файл текстового формата с нумерацией строк.
print(f'Рандомные 20 библиографических ссылок вида <автор>. <название> - <год>:')

with open("books.csv", "r") as csvfile:
    table = list(reader(csvfile, delimiter=';'))  # преобразует таблицу (типа csv) в список разделенный точкой с запятой
    random_numbers = random.sample(range(1, len(table)), 20)
    for x in random_numbers:
        print(f'{table[x][4]}. {table[x][1]} - {table[x][6]}')

# Доп. задание №1: вывести названия всех тегов из таблицы books.csv
with open("books.csv", "r") as csvfile:
    table = list(reader(csvfile, delimiter=';'))
    for row in table[1:]:
        lower_case = row[12].lower()
        index = lower_case.find(search.lower())
        row_tags = str(row[12]).split('#')
        for x in row_tags:
            if (x not in tags) and (x!=''):
                tags.append(x)
print(f'Все жанры книг из таблицы: \n {tags} \n')

# Доп. задание №2 вывести 20 самых популярных книг из таблицы
print("20 самых популярных книг из таблицы:")
with open("books.csv", "r") as csvfile:
    table = list(reader(csvfile, delimiter=';'))[1:]
    for row in table:
        if [row[8], row[1]] not in popular:
            popular.append([int(row[8]), row[1]])
    popular=sorted(popular, key = lambda x: x[0], reverse=True)[:20]
    for i in range(20):
        print(f' Книга: {popular[i][1]}, кол-во выдач: {popular[i][0]}')
