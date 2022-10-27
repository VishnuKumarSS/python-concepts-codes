a=input("Enter your mail id to verify: ")
b="@"
c="in"
c1="com"
d=" "
e="."
f=a.index("@")
g=a[f+1].isalpha()
if d in a:
    print("do not enter space mail")
elif a == "":
    print("Enter mail :)")    
elif (b in a) and (c in a or c1 in a) and (e in a):
    if g is False:
        print("Invalid mail")
    elif a.endswith(c) or a.endswith(c1) and g is True:
        print("Its valid mail")
    elif a.endswith(c) is False:
        print("Invalid mail")
else:
    print("Invalid mail")
    #print("Its valid mail")