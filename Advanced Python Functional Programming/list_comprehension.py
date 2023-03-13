#list_comprehension
list1=[char for char in 'Hello']
print(list1)

list2=[num for num in range(1,100)]
print(list2)

list3=[num*2 for num in range(1,100)]
print(list3)

list4=[num*2 for num in range(1,100) if num%2==0]
print(list4)