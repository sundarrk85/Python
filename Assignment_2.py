'''
Get Name, Email, Phone no from user and display 
Username : Name
Email : email
Phone : num
'''

name = input("Enter your name : \t")
email = input("Enter your email : \t")
Phone = int(input("Enter your Phone number : \t"))
star = '*'
print(star * 50 + '\n')
print("Name : {1}\nEmail : {0}\nPhone : {2}\n".format(email,name,Phone))
print(star * 50 + '\n')


