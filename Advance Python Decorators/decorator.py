def hello():
    print('Helloooooooooooe')

greet=hello
del hello
print(greet())



def add(func):
    func()
def mul():
    print('Multiplication')
a=add(mul)
print(a)