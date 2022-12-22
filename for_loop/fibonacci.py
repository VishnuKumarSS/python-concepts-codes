n = int(input("Enter a number for fibonacci: "))
a=0
b=1
if n==0:
    print("Enter valid number")
elif n==1:
    print(a) # or just print 0
else: 
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)


    