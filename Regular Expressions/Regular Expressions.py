import re
pattern=re.compile('this')
string='Search inside of this text please!'
print('Search' in string)

print(re.search('this',string))
a=re.search('this',string)
print(a.end())
print(a.group())
print(a.span())
print(a.start())



b=pattern.search(string)
print(b.group())