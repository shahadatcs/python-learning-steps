# tuple method  index, count

my_tuple=(1,2,2,3,4,5,6)
a,b,c, *other=(1,2,2,3,4,5,6)


print(len(my_tuple))
print(my_tuple.index(5))
print(my_tuple.count(2))
print(other)