pwd_correct = True
if pwd_correct:
    print("Logged In")
else:
    print("Incorrect Pwd")

print("IfElse ends here")


num = 27
if num % 10 == 0:
    print('{} is multiple of 10'.format(num))       # .format method
else:
    print(str(num) + ' is not multiple of 10')      # traditional printing


# else if ladder (elif)
ind_score = 360
if ind_score >= 350:
    print("India will win")
elif ind_score >= 250:
    print("India might win")
elif ind_score >= 150:
    print("Australia might win")
else:
    print("Australia will win")

'''
# nested if
# check if given num is 3 digit even number or not
n = int(input("Enter a number : "))
if n > 99 and n < 1000:
    if n % 2 == 0:
        print('{} is 3 digit even number'.format(n))
else:
    print('{} is not 3 digit even number'.format(n)) '''


# strings
name = 'Sundar'
if name[0] == 's' or name[0] == 'S':
    print("{} starts with 's'".format(name))





