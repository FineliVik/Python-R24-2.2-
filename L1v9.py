#вариант 9
import time

BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
RED = '\u001b[41m'
BLACK = '\u001b[40m'
GREEN = '\u001b[42m'


# №1 ФЛАГ ФИНЛЯНДИИ
for i in range(1, 13):
    if i!=5:
        print(f'{" "}{WHITE}{"   " * 4}{BLUE}{"   "}{WHITE}{"   " * 12}{END}')
    else:
        print(f'{" "}{BLUE}{"   " * 17}{END}')


# №2 узор i - два круга
# №2.1 - один круг
for i in range(0, 7):
    if i%6==0:
        print(f'{" "}{WHITE}{" " * 9}{BLACK}{" " * 5}{WHITE}{" " * 9}{END}')
    elif i==1 or i==5:
        print(f'{" "}{WHITE}{" " * 6}{BLACK}{" " * 11}{WHITE}{" " * 6}{END}')
    else: # 2 3 4
        print(f'{" "}{WHITE}{" " * 4}{BLACK}{" " * 15}{WHITE}{" " * 4}{END}')
# отступ (чтобы один круг и два круга не "слипались"):
print(f'{" "}{WHITE}{" " * 30}{END}')
# №2.2 - два круга
for i in range(0, 7):
    if i%6==0:
        print(f'{" "}{WHITE}{" " * 9}{BLACK}{" " * 5}{WHITE}{" " * 5}{END}' + f'{""}{WHITE}{" " * 5}{BLACK}{" " * 5}{WHITE}{" " * 5}{END}')
    elif i==1 or i==5:
        print(f'{" "}{WHITE}{" " * 6}{BLACK}{" " * 11}{WHITE}{" " * 2}{END}' + f'{""}{WHITE}{" " * 2}{BLACK}{" " * 11}{WHITE}{" " * 2}{END}')
    else: # 2 3 4
        print(f'{" "}{WHITE}{" " * 4}{BLACK}{" " * 15}{END}' + f'{BLACK}{" " * 15}{WHITE}{" " * 2}{END}')
#отступ между заданиями, чтобы черные круги не сливались с фоном консоли:
print(f'{" "}{WHITE}{" " * 30}{END}')



"""
черновик с расчетами для круга:
         11111     
      11111111111
    111111111111111
    111111111111111
    111111111111111
      11111111111
         11111

         0 1 2 3 4 5 6
9 проб + 5 цвета + 9 проб = 18+5 = 23
11 цвета => (23-11)/2 = 6 проб c каждой стороны
7+7+1 = 15 цветных => (23-15)/2 = 4 проб c каждой стороны
"""


# №4 график функции y = x/2:

plot_list = [[0 for i in range(10)] for j in range(10) ]
result_list = [i/2 for i in range(10)]

step = abs((result_list[0] - result_list[9])/9) # - единичное знач клетки (в данном случае 0.5)
# вычитаем из первого последнее в модуле и делим на кол-во интервалов

for i in range(10):
    for j in range(10):
        if j==0:
            plot_list[i][0] = step * (8-i) + step
            # В первой колонке матрицы записываются значения, которые уменьшаются от 4 до 0.

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result_list[9-j]) < step:
            #послед проверяем значения Oy и проверяем:
            #если его значение меньше, чем шаг, то заменяем
            for k in range(9):
                if 8-k == j:
                    plot_list[i][k+1] = 1
                    #перебираем строки и, когда находим нужную, то пишем 1
for i in range(9):
    line = ""
    for j in range(10):
        if j == 0:
            line += '\t' + str(plot_list[i][j])  + '\t'
        elif plot_list[i][j] == 0:
            line += "--"
        elif plot_list[i][j] == 1:
            line += "##"
    print(line)
print("\t0\t 1 2 3 4 5 6 7 8 9") #график в ширину

# №5 Числа от 5 до 10 и числа от -5 до -10, остальные отбросить
# nums - все числа из файла, открыт в начале кода
# percent - процент для диаграммы
nums = [float(i) for i in open("sequence.txt").readlines()]

percent_1 = 0
percent_2 = 0
for x in nums:
    if 10 >= abs(x) >= 5:
        if x>=5:
            percent_1 += 1
        else:
            percent_2 += 1
percent_11 = (percent_1/len(nums))*100
percent_21 = (percent_2/len(nums))*100

print(f'Процент чисел от 5 до 10 и числа от -5 до -10 относительно общего кол-ва всех чисел:\n{" "}{RED}{" " * int(percent_11)} {END} {percent_11} % \n'
      f'{" "}{BLUE}{" " * int(percent_21)} {END} {percent_21} % ')

# Процент чисел от 5 до 10 и числа от -5 до -10 относительно чисел (10 >= abs(x) >= 5):
percent_12 = (percent_1/(percent_1+percent_2))*100
percent_22 = (percent_2/(percent_1+percent_2))*100

print(f'Процент чисел от 5 до 10 и числа от -5 до -10 относительно чисел (10 >= abs(x) >= 5):\n{" "}{RED}{" " * int(percent_12)} {END} {percent_12:.1f} % \n'
      f'{" "}{BLUE}{" " * int(percent_22)} {END} {percent_22:.1f} % \n')

# №6 - доп задание
#показатель прогресса ver№1:

for i in range(100):
    print(f'\rProgress: {GREEN}[{"|" * i}]{END} {i + 1}%', end="")
    time.sleep(.5)  # для более плавного выведения
    # \r - возвращает курсор в нач строки (enter + вверх)
    # end='' - окончание каждой строки
