with open('text.txt',mode='r+') as my_file:
    text=my_file.write('Hi I am Shahadat')
    print(text)
with open('sad.txt',mode='a') as my_file:
    text=my_file.write('Hi I am Shahadat')
    print(text)
    
t= tuple(zip(zip(range(5),range(len('abc')))))
print(t)