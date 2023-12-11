# Write a program to accept a string from the user and display characters that are present at an even index number

str=input('Enter a string: ')
print(f'\nThe original string is {str}')
print(f'Printing only even index chars')
for i in str:
    if str.index(i)%2 == 0:
        print(f'{i}\n')