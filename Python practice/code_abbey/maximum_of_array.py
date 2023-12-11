array = []
no_of_items = int(input('Enter no of items in an list: '))

# getting user inputs
if no_of_items > 0:
    for i in range(no_of_items):
        array.append(int(input(f'Enter item {i+1}: ')))

    print(f'\nThe original array is: {array}')
else:
    print(f'Item count should be greater than 0')
    exit()

# logic starts
print(f'The maximum value is {max(array)} and minimum value is {min(array)}')
