# Random password generator

import random as r

print(f'Welcome to Random password generator!\n')
random_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()"
no_of_passwords = int(input("Please enter the number of passwords to the generator : "))
password_length = int(input("\nPlease enter the length of the password : "))

if no_of_passwords == 1:
    print(f'Here is your random password\n')
else:
    print(f'Here are your random passwords\n')

# logic starts
for i in range(no_of_passwords):
    password = ''
    for chars in range(password_length):
        password = password + r.choice(random_chars)
    print(f'{i+1}) {password}\n')
