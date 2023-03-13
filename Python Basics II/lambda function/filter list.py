lst = []
n = int(input('Enter a number: '))
for i in range(0, n):
    lst.append(int(input()))

lst = list(filter(lambda x:(x%2==0) , lst))
lt = list(filter(lambda x:(x%2==1) , lst))

print(lst)
