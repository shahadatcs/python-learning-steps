# python program to demonstrate in_built polymorphic function

# Built in len print
#length of string
print(len('Shahadat'))
# length of list
print(len([1,5,6])) 
# length of tuple
print(len((1,5,6)))

print(end='\n')


# Example user difined polymorphism

def add(x, y, z = 0):
    return x + y + z
 
print(add(2, 3))
print(add(2, 3, 5))

print(end='\n')


# polymorphism with class method

class square():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z   
    def area(self):
        return self.x **2
    def boundary(self):
        return 4* self.x
    def volume(self):
        return self.x **3
class retraingle():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z   
    def area(self):
        a = self.x
        b = self.y 
        return a*b
    def boundary(self):
        a = self.x
        b = self.y 
        return 2*(a+b)
    def volume(self):
        return self.x * self.y * self.z 
ob_sq = square(5,3,2)
ob_re = retraingle(5,3,2)

for cal in (ob_sq, ob_re):
    print(cal.area())
    print(cal.boundary())
    print(cal.volume())
    