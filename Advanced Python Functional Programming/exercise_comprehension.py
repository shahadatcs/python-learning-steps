some_list=['a','b','c','d','b','e','n','m','n']

duplicates=list([x for x in some_list if some_list.count(x) > 1])
print(duplicates)