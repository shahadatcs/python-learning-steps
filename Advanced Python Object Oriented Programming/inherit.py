# Single Inheritance
class animal: 
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def speak(self):
        print('Animal Speaking')
class cow(animal):
    def bark(self):
        return self.name
    def bar(self):
        return self.id
ob = cow('fox', 10)
print(ob.bark())
print(ob.speak())
print(ob.bar())
print(issubclass(cow,animal))

print(end='\n')

# Python Multi-Level inheritance
class shape():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def area(self):
        print('Calculate area of various shape')
class trangle(shape):
    def area(self):
        return .5 * self.num1 * self.num2
class retrangle(shape):
    def area(self):
        return self.num1 * self.num2
class rombos(trangle):
    def area(self):
        return self.num1 * self.num2

ob1 = trangle(20, 25)
print(ob1.area())

ob2 = retrangle(20, 25)
print(ob2.area())

ob3 = rombos(5,10)
print(ob3.area())

print(end='\n')

# Python Multiple inheritance

class calculate1():
    def sum(self, a, b):
        return a+b
class calculate2():
    def sub(self, a, b):
        return a-b
class calculate3():
    def mul(self, a, b):
        print( a*b )
class derived(calculate1, calculate2, calculate3):
    def div(self, a, b):
        return a/b
ob = derived()
print(ob.sum(12, 25))
print(ob.sub(12, 25))
print(ob.mul(12, 25))
print(ob.div(12, 3))