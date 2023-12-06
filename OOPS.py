"""
User: 

Attributes :
Username, pwd, email

Methods :                          Duname, email, pwd -> ithellam vachu seira vela thaan Methods
Register, login, changepwd

create class called User
Class - blueprint
object - instances         while creating new object the memory will be allocated

"""

# Refer "user_ClassDefined.py" file for class definition
from user_ClassDefined import User,Student,Faculty,TempFaculty,StudentFaculty
from Method_overriding import User,Student,Faculty,TempFaculty,StudentFaculty

user1 = User("Sundar","password@123")       # inga 'self' arg kuduka theva illa | User1 is object
user2 = User("Prasanna","pwd@123")
user3 = User("Saran","pswd@123")

user1.reg()         # object.method()
user2.login()

print(user1.user_name)
print(user2.user_name)
print(User.users)

tempfact1 = TempFaculty()

sf1 = StudentFaculty()





# Method overriding






