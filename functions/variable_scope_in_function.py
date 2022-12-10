# variable scope inside functions

def fun(x, y): # argument /parameter x and y 
    global a 
    a = 10 
    x,y = y,x 
    b = 20 
    b = 30 
    c = 30 
    print(a,b,x,y)


a, b, x, y = 1, 2, 3,4 
fun(50, 100) #passing value 50 and 100 in parameter x and y of function fun()
print(a, b, x, y)