#OPP
class playercharacter:
    #class object Attributes
    membership=True
    def __init__(self,name,age):
        if(self.membership):
            self.name=name #Attributes
            self.age=age
    def shut(self):
        print(f' This is my name {self.name} and age is {self.age} years')
        return 0
    def run(self):
        print(f' This is my name {self.name}.This is not orginal age {self.age} years')
        return False
    def fun(self,hello):
        print(f' This is my name {self.name}.This is not orginal age {self.age} years')
        return False
        
player1=playercharacter('Rana',45)
player2=playercharacter('Tarek',50)
print(player1.shut())
print(player1.age)

print(player2.run())
print(player2.name)
print(player2.fun('hello'))