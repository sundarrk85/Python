def happy():
    print("Jumping..")

def sad():
    print("\nCrying..")


print(happy)     # <function happy at 0x0000022675E904A0> | returns address of happy func
joy = happy      # assigning that address to another variable
joy()

print(sad)       # <function sad at 0x000001ED26198D60>
sorrow = sad
sorrow()

# Higher Order Function --> Taskes function as parameter OR Returns a function
print("\n\n")
def feeling(funcname):  # taking function as argument
    funcname()
    
feeling(happy)
feeling(sad)

print("\n\n")
def calm_down():
    print("Calm down")

def a(func_name):
    func_name()
    return calm_down
b = a(happy)
b()