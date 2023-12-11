input_a = input('Enter number or string: ')
print(f'Original input: {input_a}')
if input_a == input_a[::-1]:
    print(f'{input_a} is palindrome')
else:
    print(f'Not palindrome')