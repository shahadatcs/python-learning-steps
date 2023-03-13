#not a clean code
def is_even(num):
    if num % 2==0:
        return True
    elif num %2==1:
        return False
print(is_even(51))


#a little clean code
def is_even(num):
    if num % 2==0:
        return True
    else:
        return False
print(is_even(51))

#More a clean code
def is_even(num):
    if num % 2==0:
        return True
    return False
print(is_even(51))

#clean code
def is_even(num):
    return num % 2==0
print(is_even(51))