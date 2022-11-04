# When a class is derived from another class is called inheritance
# 5 types
# single inheritance
# multiple ,,
# multilevel ,,
# hierarchical ,,
# hybrid ,,

# subclass can access all the variables
# and functions in the parent class

class A:
    def display1(self):
        print("Base class")
class B(A):
    def display2(selff):
        print("Sub class")
obj=B() # if we type obj=A() it will show error, because we cannot call the sub class using parent class
obj.display1()
obj.display2()

# Here A is parent class or base class or super class
# and B is sub class or derived class or child class or hier class
