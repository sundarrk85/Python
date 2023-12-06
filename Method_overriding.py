class User:

    users = 0       # idhu class matum sonthamaana variable | class variable

    # self - Entha object kaaga itha call panromo antha object ah kurikithu
    # self.user_name - Entha object ah vachu call panromo antha object oda uname self la vanthu store aaidum
    
    # This is constructor
    def __init__(self,user_name,pwd):    
        self.user_name = user_name      # uname -> instance variable 
        self.pwd = pwd                  # pwd   -> instance variable
        User.users += 1                 # classname.classvariable

    # Defining Methods
    def reg(self):                      # self - must give all methods inside class
        print("Registering..." + self.user_name)
    
    def login(self):
        print("Logging in...." + self.user_name)
    
    def greet(self):
        print("Hello user")


class Student(User):  # Student class inherits User class
    
    # User - Parent class | base class | super class
    # Student - child class | derived class | sub class
    def greet(self):    # overriding method
        print("Hi student!..")

class Faculty(User):  # Faculty class inherits User class
    def greet(self):
        print("Hi teacher!..")


class TempFaculty(Faculty):
    # Multilevel inheritance
    def greet(self):
        print("Hello!..") 


# Though we have greet def in parent class User, we are again defining the greet def in child classes

# Parent class la already greet() iruku but child class la athey greet() name vachu vera mari define 
# pannikitta athu Method overriding 

# Entha class name vachu greet call panromo antha class la enna greet def iruko athu thaan exe agum




