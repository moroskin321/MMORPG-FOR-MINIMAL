from random import randint
from human import Human
class Warrior(Human):
    def set_shield(self, shield):
        self.shield = shield

    def power_increase(self, target):
        target.strength += randint(5, 10)


    def turn(self, a, target):
        if a == 1:
            self.physic_attack(target)
        elif a == 2:
            if self.mana >= 20:
                self.magic_attack(target)
            else:
                return -1
        elif a == 3:
            self.power_increase(target)
