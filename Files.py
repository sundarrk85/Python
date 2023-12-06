# mode - 'w' for write | it will overwrite the old contents and add new contents
#        'a' for append | it will add at end of the file and it won't touch old contents

with open("myfile.txt") as file:                # as "file" or "anyname"   anyname.read
    print(file.read())
print(file.closed)          # True 


txt = "I am learning Python"
with open("myfile.txt",'w') as a:
    a.write(txt)
print(a.closed)

txt = "I am learning Python"
with open("myfile.txt",'a') as a:
    a.write(txt)
print(a.closed)



with open("C:\\Users\\Sundar\\Desktop\\file.txt") as f:      # Use 2 back slashes for path                # 
    print(f.read())
print(file.closed)          # True 






