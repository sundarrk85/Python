print("You won!") # built in functions - just calling (arguments/parameters) | no return value
# name = input("What is your name?") # it returns some value

def greet():
    print("Hello")
    print("Hello world!")

greet() 
greet()
greet()



def greet(name):            # name --> parameter
    print("Hello " + name)
    print("Hello world!")

greet("Sundar")             # "Sundar" --> arguments
greet("Raja") 

def greet(fname,lname):            
    print("Hello " + fname + " " +lname)
    print("Hello world!")

greet(fname= "Sundar",lname="R K")

# sum of n natural numbers
def sum(n):
    result = n * (n+1)/2
    return result

print('The sum of numbers is {}'.format(sum(25)))






