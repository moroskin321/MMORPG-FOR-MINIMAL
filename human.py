from random import randint
class Human:
    hp = 500 #жизни
    mana = 100 #кол-во магической энергии
    strength = 10  #сила атаки
    magic_strength = 120 #урон от магии

    def __init__(self, hp, mana, s, ms):
        self.hp = hp
        self.mana = mana
        self.strength = s
        self.magic_strength = ms

    def get_dmg(self, dmg):
        self.hp = self.hp - dmg

    def physic_attack(self, enemy):
        enemy.get_dmg(self.strength)
        self.mana += 5

    def magic_attack(self, enemy):
        if self.mana >= 20:
            enemy.get_dmg(self.magic_strength)
            self.mana -= 20




    def __str__(self):
        s = '#'*80
        s = s + '\nкол-во хп = {}\nкол-во маны = {}\nфизическая сила = {}\nмагическая сила = {}\n'.format(self.hp, self.mana, self.strength, self.magic_strength) + s
        return s

    def is_alive(self):
        if self.hp <= 0:
            return False
        else:
            return True
