# Для варианта 9 :
backpack = []
inventory = [['empty' for _ in range(4)] for _ in range(2)]  # инвентарь
size_backpack = 2*4  # размер рюкзака (2*4)
weight = 0  # общий вес в рюкзаке
points = 20  # начальное количество очков
total_points = points  # итоговое количество очков выживания

# Предметы и их ценность
items = [
    ('r', 3, 25),  # Винтовка (rifle)
    ('p', 2, 15),  # Пистолет (pistol)
    ('a', 2, 15),  # Боекомплект (ammo)
    ('m', 2, 20),  # Аптечка (medkit)
    ('i', 1, 5),   # Ингалятор (inhaler)
    ('k', 1, 15),  # Нож (knife)
    ('x', 3, 20),  # Топор (axe)
    ('t', 1, 25),  # Оберег (talisman)
    ('f', 1, 15),  # Фляжка (flask)
    ('d', 1, 10),  # Антидот (antidot)
    ('s', 2, 20),  # Еда (supplies)
    ('c', 2, 20)   # Арбалет (crossbow)
]

# Сортируем предметы
sorted_items = sorted(items, key=lambda x: x[2] / x[1], reverse=True)

# Ищем и добавляем антидот в рюкзак
for item in sorted_items:
    if item[0] == 'd':
        backpack.append(item)
        weight += item[1]
        total_points += item[2]
        sorted_items.remove(item)  # Удаляем антидот из списка, чтобы не добавлять его повторно

# Добавляем другие предметы в рюкзак
for item in sorted_items:
    if weight + item[1] <= size_backpack:
        backpack.append(item)
        weight += item[1]
        total_points += item[2]

# Уменьшаем очки за не добавленные предметы
for item in sorted_items:
    if item not in backpack and weight + item[1] > size_backpack:
        total_points -= item[2]

# Заполняем инвентарь
number_slot = 0 # кол-во предметов в ИТОГОВОМ инвентаре inventory
for j in range(len(backpack)):
    nums = backpack[j][1] # кол-во ячеек, которое занимает предмет
    for l in range(nums):
        if number_slot < size_backpack:  # Проверяем, что не превышаем размер инвентаря
            x = number_slot // 4
            y = number_slot % 4
            inventory[x][y] = backpack[j][0]
            number_slot += 1

# Результаты для варианта 9:
if total_points > 0:
    print('Весь инвентарь (2*4):')
    for i in inventory:
        print(i)
    print(f'Очки выживания: {total_points}')
else:
    print('Количество очков выживания отрицательное')
