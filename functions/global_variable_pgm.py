#Global variable program: 
def fun(): 
    global s #accessing/making global variable for fun() 
    print(s) 
    s = "I love India!" #changing global variable’s value 
    print(s)
s = "I love world!" 
fun()
print(s)