#break_continue_pass

#break
my_list=[1,2,3]
for item in my_list:
    print(item)
    break

i=0
while i < len(my_list):
    print(my_list[i])
    i+=1
    break

#continue
my_list=[1,2,3]
for item in my_list:
    print(item)
    continue

i=0
while i < len(my_list):
    print(my_list[i])
    i+=1
    continue

#pass

my_list=[1,2,3]
for item in my_list:
    print(item)
    pass

i=0
while i < len(my_list):
    print(my_list[i])
    i+=1
    pass