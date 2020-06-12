from human import Human
class Mag(Human):
    def heal(self, target):
        if self.mana >= 10:
            target.hp += randint(10, 20)

    def turn(self, a, target):
        if a == 1:
            self.physic_attack(target)
        elif a == 2:
            if self.mana >= 20:
                self.magic_attack(target)
            else:
                return -1
        elif a == 3:
            if self.mana >= 10:
                self.heal(target)
            else:
                return -1
