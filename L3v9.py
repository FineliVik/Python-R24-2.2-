import random
import tkinter as tk
from tkinter import PhotoImage
import pygame

"""
ВАЖНО!
Перед запуском сохранить из репозитория в отдельную папку с кодом:
background2.png
image1.png
music.mp3
"""

alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cancel():
    window.destroy()

def generate():
    num1 = str(random.randint(1, 26)).zfill(2)  # Первое рандомное число
    num2 = str(random.randint(1, 26)).zfill(2)  # Второе рандомное число
    number1 = max(int(num1), int(num2))  # Наибольшее рандомное число
    number2 = min(int(num1), int(num2))  # Наименьшее рандомное число
    block = []  # Блок из букв от первого до второго числа (рандомно)
    for i in range(7):
        block.append(str(random.choice(alf[number2:number1 + 1])))
    print(f'{alf[number2:number1 + 1]}')
    key_label.configure(text=f'{str(number2).zfill(2)} {"".join(block)} {str(number1).zfill(2)}')

# Окно
window = tk.Tk()
window.title("Key Generator")
window.geometry("1080x650")

# Фон
background_image = tk.PhotoImage(file="background2.png")
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Картинка
header_image = PhotoImage(file="image1.png")
header_image = header_image.subsample(1,1)
header_label = tk.Label(window, image=header_image)
header_label.place(relx=0.5, rely=0.05, anchor='n')

# Сгенерированный ключ
key_label = tk.Label(window, text="", font=('Consolas', 20), bg='white')
key_label.place(relx=0.5, rely=0.55, anchor='s')

# Создание фрейма для кнопок
btn_frame = tk.Frame(window)
btn_frame.place(relx=0.5, rely=0.85, anchor='s')

# Кнопки "закрытия" и "генерации ключа":
btn_guess = tk.Button(btn_frame, text='"Сгенерировать произвольный ключ"', width=30, command=generate)
btn_guess.pack(side=tk.LEFT, padx=5)

btn_cancel = tk.Button(btn_frame, text='Cancel', width=15, command=cancel)
btn_cancel.pack(side=tk.LEFT, padx=5)

#Музыка:
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

window.mainloop()
