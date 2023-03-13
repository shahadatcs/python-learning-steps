import re
string = 'Fruits 32, Animal 80, cars 34'
pattern = '\D+'
match = re.findall(pattern, string)
print(match)