# function
def add_ten(num):
    return num + 10
print(f'The output is {add_ten(20)}')
print('The output is {}'.format(add_ten(20)))

# Lambda - anonymous function
# cannot write for large functions
# lambda (arg passing to function):expression to be returned
# lambda = par1, par2, par3, .... parN : expression
a = lambda x: x + 10  
print(f'\nThe output using lambda function is {a(15)}')



product = lambda x, y, z : x*y*z
print(f'\nThe output is {product(5,4,6)}')

tall_enough = lambda h : h>175   # returns True or False
print(f'\nThe output is {tall_enough(156)}')

strong_enough = lambda w : "yes" if w>70 else "no"      # using if else
print(f'\nThe output is {strong_enough(70.1)}')

