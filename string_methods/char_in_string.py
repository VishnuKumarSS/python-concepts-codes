# to find character in a string

a =input("Enter a string: ")
b =input("Enter a character to find in a string: ")
c=a.find(b) # this returns -1 if not found
if a=="" or a==" ":
    print("Enter a valid string")
elif b=="" or b==" ":
    print("Enter a valid character :)")
elif c!= -1:
    print("Its found")
else:
    print("Not found")

# we can also use the code below
""" 
c=a.count(b)
if c == 0:
    print("Not found")
else:
    print("Its found"""