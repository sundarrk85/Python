# Return the count of a given substring from a string
str = input('Enter a string: ')
sub_str = input('Enter a substring to be searched: ')

if len(sub_str) < len(str):
    if str.find(sub_str) != -1:
        print(f'{sub_str} appeared {str.count(sub_str)} times in given string')
    else:
        print(f'Substring not found in {str}')
else:
    print(f'SUb string length should not exceed string length')
