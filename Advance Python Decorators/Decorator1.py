def my_decorator(func):
    def wrap_fun():
        print('*********')
        func()
        print('I am fine')
    return wrap_fun
@my_decorator
def hello():
    print('helloooooooo')

hello()

#function likes Decorators
a=hello

a()
    
    
#Again
b=my_decorator(hello)
b()