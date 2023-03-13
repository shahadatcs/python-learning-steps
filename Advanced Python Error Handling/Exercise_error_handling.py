while True:
    try:
        age=int(input('What is your age: '))
        10/age
    except ValueError:
        print('Enter a numeric value: ')
        #continue
    except ZeroDivisionError:
        print('Enter a higher value then one: ')
        break
    else:
        print('thank you')
        break
    finally:
        print('OK, I am finally done')
    print('Can you here me')