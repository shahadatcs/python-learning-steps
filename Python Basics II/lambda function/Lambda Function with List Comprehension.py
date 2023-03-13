square = [lambda num=num : num**2 for num in range(1, 20)]
for squr in square:
    print(squr(), end=' ')