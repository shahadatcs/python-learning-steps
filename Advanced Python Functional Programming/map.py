my_list=[1,2,3]
def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, my_list)))
print(my_list)
print(tuple(map(multiply_by2, my_list)))
print(set(map(multiply_by2, my_list)))
#print(dict(map(multiply_by2, my_list))) #Does not convert 



