class Student:  
    # Constructor - parameterized  
    def __init__(self, name):  
        print("This is parametrized constructor")  
        self.name = name  
    def show(self):  
        a = self.name
        a = a[ : : -1]
        return a
        
          
          
student = Student("John")  
p = student.show()
print(p)    
print(end ='\n')

# Python Non-Parameterized Constructor
class student:
    def __init__(self):
        print('Python Non-Parameterized Constructor')
        
    def show(self, name):
        a = name
        return a
st = student()
print(st.show('Shahadat'))
print(end ='\n')
# Python Default Constructor
class student:
    name ='Shahadat'
    id = 160148
    def __init__(self):
        print('Python Default Constructor')
    def show(self):
        a = self.name
        b = self.id
        return a, b
st = student()
print(st.show())

print(end ='\n')

# More than One Constructor in Single class
class student:
    def __init__(self):
        print(' This is first Constructor')
        
    def __init__(self):
        print(' This is Second Constructor')    
        
st = student()

print(end ='\n')

# More than One Constructor in Single class
class student:
    def __init__(self, name):
        self.name = name
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
#st = student('Shahadat')
st = student('Shahadat', 160148 )
print( st.name, st.id)
print(st.__dir__)
print(st.__class__)
print(st.__dict__)
print(st.__doc__)
print(st.__eq__)
print(st.__format__)
print(st.__getattribute__)
print(st.__module__)
print(st.__init__)
print(st.__reduce__)


