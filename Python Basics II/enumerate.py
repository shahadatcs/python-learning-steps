# enumerate that display index and value at a time 
for i, char in enumerate('hello'):
    print(i,char)
for i, char in enumerate(list(range(100))):
    #print(i,char)
    if char==50:
        print(f' The index of 50 is:{i} ')