lst =[ 2,5,8,9,7]
square_list = list(map(lambda x: x*x, lst))
square_list.reverse()
square_list.sort()
print(square_list)