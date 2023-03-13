#Decorator Pattren
def my_decorator(func):
    def wrap_fun(*args,**kwargs):
        print('*********')
        func(*args,**kwargs)
        print('123456789')
    return wrap_fun
@my_decorator
def hello(greeting, emoji=':('):
    print(greeting,emoji)
hello('hiii')