class playercharacter:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def run(self):
        print('run')
        return 'done'
player1=playercharacter('Monkey',12)
player2=playercharacter('Lion',25)
player2.attak=50
print(player1.name)
print(player2.attak)
print(player2.age)
print(player1.run())


        