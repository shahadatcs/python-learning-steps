#formatted string

name='Shahadat'
age=28

print(f'This is {name} Hossain. it\'s {age} years old.') #python3 version
print('This is '+ name + 'Hossain. It\'s '+ str(age) + ' years old.')
print('This is {} Hossain. It\'s {} years old.' .format(name,age))
print('This is {0} Hossain. It\'s {1} years old.' .format(name,age))

print('This is {new_name} Hossain. It\'s {age} years old.' .format(new_name='Sharmin',age=27))