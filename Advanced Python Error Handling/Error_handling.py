#Error Handling

while True:
    try:
        age=int(input('What is yor age?: '))
        10/age
    except ValueError:
        print('Please input a numeric number: ')
    except ValueError:
        print('!!!!!')
    except ZeroDivisionError:
        print('Enter age higher than zero: ')
    else:
        print('Thank you')
        break