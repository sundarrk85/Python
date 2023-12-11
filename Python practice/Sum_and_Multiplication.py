# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

a=int(input(f'Enter 1st input: '))
b=int(input(f'\nEnter 2nd input: '))

if a*b>1000:
    print(f'\nThe sum is {a+b}')
else:
    print(f'The product is {a*b}')

