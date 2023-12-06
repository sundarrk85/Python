# Refer "OOPS.py" file for this class usage

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


class Student(User):  # Student class inherits User class
    
    # User - Parent class | base class | super class
    # Student - child class | derived class | sub class
    def greet_student(self):
        print("Hi student!..")

class Faculty(User):  # Faculty class inherits User class
    def greet_faculty(self):
        print("Hi teacher!..")


class TempFaculty(Faculty):
    # Multilevel inheritance
    def greet_Tempfaculty(self):
        print("Hello!..") 




# Multiple inheritance
class StudentFaculty(Student,Faculty):  # inherits more than 1 class
    pass        # nothing -> pass






