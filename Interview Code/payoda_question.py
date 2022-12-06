#multiplication without using * operator

def mul(a,b):
    c=0
    for i in range(b):
        c += a
    print(c)

a=int(input("Enter a number"))
b=int(input("Enter a number"))
mul(a,b)


