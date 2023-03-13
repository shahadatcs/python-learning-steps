#OOP
class user():
    def sign_in(self):
        print('logged in')
class wizard(user):
    def __init__(self,name,power):
        self.name=name
        self.power=power
    def attack(self):
        print(f'Attacking with power of {self.power}')
class Archer(user):
    def __init__(self,name,num_arrows):
        self.name=name
        self.num_arrows=num_arrows
    def attack(self):
        print(f'Attacking with arrows of {self.num_arrows}')

wizard1=wizard('Monkey',25)
archer1=Archer('Lion',60)

for char in [wizard1,archer1]:
    char.attack()

def player_attack(char):
    char.attack()
player_attack(wizard1)
player_attack(archer1)


print(dir(wizard1))