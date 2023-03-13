#scope_rules

#start with local
#parent local 
#Global
#Building in python function
a=1

def parent():
    def fun():
        a=10
    return fun()

print(parent())
print(a)