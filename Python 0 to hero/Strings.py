a='hello world'

a.capitalize()      
# Hello world

a.casefold()        
# hello world - same as lower() 

a.center(20,'*')    
# '****hello world*****' / a.center(20) - returns space instead of '*'

a.count('h')        
# 1 time 'h' present

a.endswith('d')     
# returns T or F 

a.expandtabs(2)     
# a='h\te\tl\tl\to - a.expandtabs() - Default size = 8 (7 spaces between characters)

a.find('h')         
# returns the position. 
# If char not found returns -1
# a.find('h',5,10) - searches between 5th and 10th index

# format()
a = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
b = "My name is {0}, I'm {1}".format("John",36)
c = "My name is {}, I'm {}".format("John",36)

a.index('q')
# Returns position of string. If not found it throws error

a.isalnum()
# Returns T if A-Z and 0 - 9. Excluding special characters (space also)

a.isalpha()
# Returns T if A-Z. No special characters & numbers

a.isascii()
# T if ascii characters

a.isdecimal()
# T if all characters are decimal

a.isdigit()
# T if all characters are digits
