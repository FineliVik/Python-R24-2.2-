import cv2

# Загрузка изображения
img = cv2.imread('variant-9.png')

assert img is not None, "Файл не найден, проверьте путь к изображению."

# Создание пирамиды изображений
pyramid = [img]
for i in range(4):  # Создаем 4 уровня пирамиды
    img = cv2.pyrDown(img)  # Уменьшаем изображение в 2 раза
    pyramid.append(img)

# Отображение пирамиды
for i, level in enumerate(pyramid):
    cv2.imshow(f'Level {i}', level)

cv2.waitKey(0)
cv2.destroyAllWindows()