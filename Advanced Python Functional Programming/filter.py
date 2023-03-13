#filter
my_list=[1,2,3]
def multiply_by2(item):
     return item*2
def only_check(item):
    return item % 2 !=0

print(list(map(multiply_by2,my_list)))
print(list(map(only_check,my_list)))

print(list(filter(multiply_by2,my_list)))
print(list(filter(only_check,my_list)))
 