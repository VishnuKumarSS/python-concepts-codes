'''Runtime polymorphism in python
********************************
It is called “dynamic binding”.
It is method “overriding technique”.
Overriding is the concept of defining a method in
Child class with the same name and same set of
arguments in Parent class method.
A Child object can shows the functionality of
Parent and Child. Hence it is called Polymorphic'''
class Grand:
    def fun(self):  
        print("Grand")
        return
class Parent(Grand):
    def fun(self):
        print("Parent")
        return
class Child(Parent):
    def fun(self):
        print("Child")
        return
class Override:
    def main():
        object = Child()
        object.fun()
        super(Child,object).fun() # super is the function in python
        super(Parent,object).fun()
        return
Override.main()
