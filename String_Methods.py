# 1. capitalize()
cap1 = 'hello'
cap2 = 'HEllo'
print(f'capitalize() - {cap1.capitalize()} and {cap2.capitalize()}')

# 2. casefold()
cas1 = 'MARIo'
cas2 = 'maRIO'
print(f'\ncasefold() - {cas1.casefold()} and {cas2.casefold()}')

# 3. center()
cen1 = 'Sundar'
print(f"\ncenter - {cen1.center(20)}")
print(f"\ncenter - {cen1.center(20,'*')}")

# 4. count()
cou = 'abc_abc_abc_abc'
print(f"\ncount - {cou.count('ab')}")

# 5. encode() - getting byte version of str
enc = 'Elon Musk'
print(f"\nencode - {enc.encode(encoding='UTF-8',errors='strict')}")

# 6. endswith()
endw = 'apple'
print(f"\nendswith - {endw.endswith('e')}")
print(f"\nendswith - {endw.endswith(('e','a'))}")   # endswith 'e' or 'a'

# 7. expandtabs()
exptab = 'txt1\ttxt2\ttxt3'
print(f"\nexpandtabs - {exptab.expandtabs(20)}")

# 8. find()
fnd = 'Remember to comment and subscribe'
position = fnd.find('subscribe')
print(f"\nfinding first occurence in str - {position}")
print(f"\nprinting - {fnd[position:]}")
position = fnd.find('asdas')        # asdas - not in the str
print(f"\nfinding first occurence in str - {position}")
print(f"\nprinting - {fnd[position:]}")

# 9. format()
s1 = '{subject} is doing: {action}'
print('\n')
print(s1.format(subject='Cat',action='meow')) 
s1 = '{} is doing: {}' # alternative
print('\n')
print(s1.format('Cat', 'meow'))









