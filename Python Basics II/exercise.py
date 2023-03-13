is_magician= False
is_expert= True

if  is_expert and is_magician:
    print('You are a master in magician')
elif is_magician and not is_expert:
    print('At least you are a getting  magician')
elif not is_magician:
    print('You need magic power')




def printNos(initial, last):
    if(initial<=last):
        print(initial, end=' ')
        printNos(initial+1,last)
n=int(input())
printNos(1,n)