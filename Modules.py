# math - it does math related functions | in math module they have defined math related function only
import Email_module as E
print(E.otp())
print(E.activation())


from Email_module import otp, activation   # (or) from Email_module import *
print(otp())
print(activation())

# refer Python module documentation



