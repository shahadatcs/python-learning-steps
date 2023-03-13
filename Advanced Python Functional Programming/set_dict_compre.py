
#Set Comprehension
set1={char for char in 'HELLO'}
print(set1)

set2={num for num in range(1,100)}
print(set2)

set3={num**2 for num in range(1,100)}
print(set3)

set4={num*2 for num in range(1,100) if num%2==0}
print(set4)


#Dictionary Comprehension


simple_dict={
    'a':1,
    'b':2
}

my_dict={key:value*2 for key,value in simple_dict.items() if value%2==0}
print(my_dict)

dict1={num:num*2 for num in ['a','b','c']}
print(dict1)