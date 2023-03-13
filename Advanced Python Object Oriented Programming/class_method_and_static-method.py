class playercharacter:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def adding_thing(cls,num1,num2):
        return cls('Monkey',num1+num2)
    
    @staticmethod
    def sub_thing(a,b):
        return a+b


#player1=playercharacter(2,3)
player1=playercharacter.adding_thing(2,3)
print(player1.name)
player2=playercharacter.sub_thing(2,3)
print(player2)