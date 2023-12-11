# Write a program to remove characters from a string starting from zero up to n and return a new string.

str=input('Enter a string: ')
no_of_char= int(input('\nEnter number of character to be removed :'))

if int(no_of_char) < len(str):
    print(f'String after removal of characters is: {str[no_of_char:]}')
else:
    print(f'Character length exceeds string length')