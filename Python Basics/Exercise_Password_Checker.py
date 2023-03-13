#Exercise Password Checker

username=input('What is your name ')
password=input('Please input a strong password ')
password_length=len(password)
hidden_password='*' * password_length

print(f'{username}, your password {password} and hide password {hidden_password} is {password_length} letter long ')