import random
class weapon:
    def __init__(self,name,power):
        self.name=name
        self.power=power
    def get_power(self):
        return self.power
class monster:
    def __init__(self,name,heath,wname,power):
        self.name=name
        self.health=heath
        self.weapon=weapon(wname,power)
    def get_power(self):
        return self.weapon.get_power()
    def get_name(self):
        return self.name
    def get_health(self):
        return self.health
    def take_damage(self,damage):
        self.damage=damage
        self.health-=self.damage
        if self.health<0:
            self.health=0

    def attack(self,monster):

        getenergy=random.randint(0,self.weapon.get_power())
        monster.take_damage(getenergy)



monster1=monster('loki',150,'axe',15)
monster2=monster('thor',100,'sword',10)
round_no=1
print(f'initial health of {monster1.get_name()} is {monster1.get_health()}')
print(f'initial health of {monster2.get_name()} is {monster2.get_health()}')
while monster1.get_health()>0 and monster2.get_health()>0:
    print('round  %d begains'%round_no)
    if random.choice([True,False]):
        attacker=monster1
        defender=monster2
    else:
        attacker=monster2
        defender=monster1
    attacker.attack(defender)
    print(f'attacker {attacker.get_name()} attacks  {defender.get_name()}')
    print(f'defender {defender.get_name()} has health {defender.get_health()}')
    if attacker.get_health()<=0 or defender.get_health()<=0:
        break

    defender.attack(attacker)
    print(f'attacker {defender.get_name()} attacks  {attacker.get_name()}')
    print(f'defender {attacker.get_name()} has health {attacker.get_health()}')
    if attacker.get_health() <= 0 or defender.get_health() <= 0:
        break

    round_no+=1

if monster1.get_health()<=0:
    print('monster  %s win'%monster2.get_name())
elif monster2.get_health()<=0:
    print('monster  %s win' % monster1.get_name())

