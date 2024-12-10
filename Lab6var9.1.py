class Player:
    def __init__(self, health, stamina, damage, price):
        self.health = health        # Количество здоровья
        self.stamina = stamina      # Количество выносливости
        self.damage = damage        # Наносимый урон
        self.price = price          # Цена одного удара
    def number_of_hits(self):
        all_hits = self.stamina // self.price
        return all_hits
class Enemy(Player):
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage
    def number_of_hits_to_kill_enemy(self, player_object):
        hits_kill_enemy =  self.health//player_object.damage
        return hits_kill_enemy
class Boss(Player):
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage
    def number_of_hits_to_kill_Boss(self, player_object):
        hits_kill_Boss = self.health // player_object.damage
        return hits_kill_Boss

player = Player(health=100, stamina=70, damage=20, price=10)
enemy = Enemy(health=100, damage=10)
boss = Boss(health=250, damage=20)

number_Player = player.number_of_hits()
number_Enemy = enemy.number_of_hits_to_kill_enemy(player)
number_Boss =  boss.number_of_hits_to_kill_Boss(player)
print(f'Персонаж может нанести всего {number_Player} ударов(а) с полной выносливостью')
print(f'Персонаж может убить врага за {number_Enemy} ударов(а)')
print(f'Персонаж может убить боса за {number_Boss} ударов(а)')



