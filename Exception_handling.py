# divide by zero




# if we know that some piece of code might result in error then that can be given in "try" block
try:
    n = int(input("Enter numerator : "))
    d = int(input("Enter denominator : "))
    a = n/d
    # print(a)
    # print('bye')
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Enter only numbers")
except Exception:       # General error
    print("some error occured")
else:
    print(a)  # if no error has occured then do this 
finally:
    print("This always executes")    # finally - error vanthalum varatiyum idhu print pannanum

print('bye')