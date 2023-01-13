# in python call by reference can be done by passing mutable objects to function as an argument
#  these are mutable objects (e.g) list,set,dictionary
a = [1,"hellow","    ",888,"python"]
b = {1,"hello world"}

def callbyreference(a,b):
    a.append("changed list")
    b.add("changed set")
    return a,b
print("values before calling function : ",a,b) 
print("After call by reference: ",callbyreference(a,b))
print("values after calling function: ",a,b) # this also changed unlike call by value

