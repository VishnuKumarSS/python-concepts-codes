# global variables in nested functions

def fun1(): 
    x = 100 
    def fun2(): 
        global x 
        x = 200
    print("Before calling fun2: " + str(x)) 
    print("Calling fun2 now:") 
    fun2() 
    print("After calling fun2: " + str(x))
fun1()
print("x in main: " + str(x))