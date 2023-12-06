def welcome(name):
    print("Welcome " + name)

welcome("Sundar")

# "name" variable scope is inside the welcome function only (local variable)
# Global varialble should be given before all the function definitions

num = 10
while num <=100 :
    print(num)
    num += 10


a = 5
def func():
    global a
    a = 10
    print(a)

func()
print(a)




# variable length arguments
# If we don't know how many arguments needed to pass to function
# use def func(*args) | can give any name after '*' | (*a)....
# whatever the arguments we are sending it will store the values passed inside "tuple"

def total(*args):
    a = 0
    for i in args:      # looping the tuple items to add all numbers
        a = a + i
    return a
print(total(4,5))                               # passing 2 args
print(total(4,5,158,1456,5))                    # passing 5 args
print(total(4,5,5,5,5,5,5,5,5,5,5,8,9,4,2))     # passing n args





# kwargs
# it will pack all the arguments in a dictionary
def print_address(**kwargs):
    for key,val in kwargs.items():
        print(val)

print_address(door_no="93",street_name="CBI colony",area="Kanthanchavadi",city="Chennai")



