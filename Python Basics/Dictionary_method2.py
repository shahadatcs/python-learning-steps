dic={
    'basket':[1,2,3],
    'greet':'hello',
    'age':20
    
}

print('basket' in dic) #check true or false
print('age' in dic.keys())
print('hello' in dic.values())
print( dic.items())
print( dic.copy())

print(dic.pop('age'))
print(dic.popitem())
print(dic.update({'age':50}))