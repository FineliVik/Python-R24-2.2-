import re

#Задача 1: Вариант 9. Все слова, оканчивающиеся на букву «e»; все числа в круглых скобках
file_txt = open('task1-ru.txt', encoding = 'utf-8').read()
result_for_words = re.findall(r'\b\w*е\b', file_txt) # \b - граница слова, * - любое кол-во букв (\w) перед 'е', \b - вторая граница слова
result_for_numbers =  re.findall(r'\(([\d.,]+)\)', file_txt) #выдает числа внутри скобок

print(f'Все слова оканчивающиеся на букву "е": {result_for_words}')
print(f'Все числа в круглых скобках: {result_for_numbers}')

#Задача 2: Вариант 9. Все размеры изображений.
file_html = open('task2.html', encoding = 'utf-8').read()
result_for_html_file =  re.findall(r'sizes="(\d+x\d+)"', file_html) #\d - границы ЧИСЕЛ и + - это любое их кол-во внутри, а между ними "x"
print(f'Все размеры изображений: {result_for_html_file}')

#Задача 3: Вариант 9. Таблица
file_csv = open('task3.txt', encoding = 'utf-8').read()

result_for_csv_file_emails = re.findall(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', file_csv) #
print(f'Электронные почты: \n{result_for_csv_file_emails}') # Дааааа, тут не получилось

result_for_csv_file_surnames = re.findall(r'\b[A-Z][a-z]+(?:[-\s][A-Z][a-z]+)?\b', file_csv)
print(f'Фамилии: \n{result_for_csv_file_surnames}')

result_for_csv_file_dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', file_csv)
print(f'Даты регистрации: \n{result_for_csv_file_dates}')

result_for_csv_file_websites = re.findall(r'https?://[^\s]+', file_csv)
print(f'Сайты: \n{result_for_csv_file_websites}')

result_for_csv_file_identifiers = re.findall(r'\b\d+\b', file_csv)
print(f'Идентификаторы: \n{result_for_csv_file_identifiers}')

table = [['Электронные почты', result_for_csv_file_emails], ['Фамилии', result_for_csv_file_surnames],
         ['Даты регистрации', result_for_csv_file_dates], ['Сайты', result_for_csv_file_websites],
         ['Идентификаторы', result_for_csv_file_identifiers]] # - таблица в списке
