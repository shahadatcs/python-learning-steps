'''
def fib1(num):
    a=0
    b=1
    for i in range(num):
        yield a
        temp=a
        a=b
        b=temp+a
for i in fib1(10):
    print(i)
'''
    
    
def fib2(n):
    a=0
    b=1
    result=[]
    for i in range(n):
        result.append(a)
        temp=a
        a=b
        b=temp+b
    return result

print(fib2(20))
