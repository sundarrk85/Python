name = 'hari'
like2 = 'apples'
like1 = 'bananas'

print('{} likes {} and {}'.format(name,like1,like2))
print('{0} likes {2} and {1}'.format(name,like1,like2))
print('{name} likes {fruit1} and {fruit2}'.format(name = 'Sundar',fruit1 = 'Apple' ,fruit2 = 'Banana'))

# {} --> placeholder


# padding
print('******{msg}*****'.format(msg='Welcome'))
print('******{msg:20}*****'.format(msg='Welcome'))     # welcome + 13spaces = 20
print('******{msg:<20}*****'.format(msg='Welcome'))    # left align - welcome
print('******{msg:>20}*****'.format(msg='Welcome'))    # right align - welcome
print('******{msg:^20}*****'.format(msg='Welcome'))    # center align - welcome



# formatting numbers
pi = 3.14159
print('The value of pi is {}'.format(pi))
print('\nThe value of pi is {:.3f}'.format(pi))

num = 100000
print('The value of num is {:,}'.format(num))        # comma  --> 100,000

a = 101
print('The binary value of a is {:b}'.format(a))        # b for binary  --> 1100101
print('The Octal value of a is {:o}'.format(a))        # o for octal  --> 145
print('The hexa value of a is {:x}'.format(a))        # x (or X) for hexa  --> 65
print('The scientific notation value of a is {:E}'.format(a))        # E for scientific notation  --> 1.010000E+02








 



