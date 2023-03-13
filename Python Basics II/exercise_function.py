#exercise_function
def highlight_even(num):
    even=[]
    for item in num:
        if item % 2==0:
            even.append(item)
    return max(even)
print(highlight_even([4,2,6,9,7,10,2,5,14,26,95,86,67,54]))
