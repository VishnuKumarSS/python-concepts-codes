# in python call by value can be done by passing immutable objects to function
# these are immutable objects (e.g) int,float,string,tuples
a = "hellow world" # string
b = 1011 # whole number or float
#c = (1,"hellow") # tuple

def callbyvalue(a,b):
    a += " python"
    b += 20
    return a,b
print("values before calling function : ",a,b) 
print("After call by value: ",callbyvalue(a,b))
print("values after calling function : ",a,b) # this is not changed unlike call by reference

