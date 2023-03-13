from functools import reduce
my_list=[1,2,3,4]

def accumulator(acc,item):
    print(acc,item)
    return acc-item
print(reduce(accumulator,my_list,10))