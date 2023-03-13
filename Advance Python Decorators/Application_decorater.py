#performance check in Decorator

from time import time 

def performance(func):
    def wrap_fun(*args,**kwargs):
        t1=time()
        result=func(*args,**kwargs)
        t2=time()
        print(f'took{t2-t1} s')
        return result
    return wrap_fun
@performance
def long_time():
    for i in range(1000000):
        i*5
long_time()