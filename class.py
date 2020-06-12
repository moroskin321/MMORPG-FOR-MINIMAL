from random import randint
from mag import Mag
from warrior import Warrior

#выбор класса
print('''Здравствуйте, выберите вашего персонажа(бета 1.2)
P.S. Игра сделана за 4.5 часа не удивляйтесь что все через одно место''')
choose = int(input('Введите 1 для Мага, 2 для Воина, 3 для рандома: '))
while True:
    if choose == 1:
        player = Mag(randint(450, 900), randint(80, 160), randint(5, 15), randint(200, 300))
        print("Вы маг")
        break
    elif choose == 2:
        player = Warrior(randint(650, 1100), randint(40, 120), randint(100, 120), randint(20, 30))
        print("Вы воин")
        break
    elif choose == 3:
        choose = randint(1, 2)
    else:
        print('Error')
        choose = int(input('Введите 1 для Мага, 2 для Воина, 3 для рандома: '))
print(player)


#Генерация противника
random_enemy = randint(1, 2)
if random_enemy == 1:
    enemy1 = Mag(randint(450, 900), randint(80, 160), randint(5, 15), randint(200, 300))
    print("Противник это маг")
elif random_enemy == 2:
    enemy1 = Warrior(randint(650, 1100), randint(40, 120), randint(100, 120), randint(20, 30))
    print("Противник это воин")
print(enemy1)

#Начало боя
i = 0
while player.is_alive() and enemy1.is_alive():
    i += 1
    print('ход номер ' + str(i))
    print('1 чтобы атаковать\n2 атака магией\n3 Специальная способность')
    a = int(input())
    print('выбери цель\n0 ты\n1 враг')
    target = int(input())
    if target == 0:
        target = player
        player.turn(a, target)
        print(target)
    else:
        target = enemy1
        player.turn(a, target)
        print(player)
        print(target)


    z = randint(1,3)
    if z == 3:
        target = enemy1
        player.turn(3, target)
        print(target)
    else:
        target = player
        player.turn(z, target)
        print(target)
        print(enemy1)


if enemy1.is_alive():
    print('ВЫ ПРОИГРАЛИ')
else:
    print('ВЫ ПОБЕДИЛИ Ъъ')
