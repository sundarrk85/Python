#By default the input we are entering is of str type, we have to change the type if needed

height = float(input("What's your height?\n"))
print(height/2.54)     #178 - Ans wil be 70.07874015748031

a = '{:.2f}'.format(height/2.54)    #To cut the decimal places 

print('After cutting off the decimal places The Height in inches is {}'.format(a))