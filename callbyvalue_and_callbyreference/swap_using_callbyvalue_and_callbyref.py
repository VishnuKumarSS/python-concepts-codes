# swapping using call by value in python
a=10
b=20


def swap1(a,b):
    a,b=b,a
    print("Inside function: ",a,b)


print("call by value: ")
print("Before calling: ",a,b)
swap1(a,b)
print("After calling: ",a,b)


# swapping using call by reference
lis=[]
lis.append(a)
lis.append(b)
#print(lis)


def swap2(lis):
    lis.reverse()
    print("Inside function: ",lis)


print("call by reference: ")
print("Before calling: ",lis)
swap2(lis)
print("After calling: ",lis)