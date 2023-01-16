# When a method with the same name and arguments is used in both a derived class and a base or super class, we say that the derived class method "overrides" the method provided in the base class.

# When the overridden method gets called, the derived class's method is always invoked. The method that was used in the base class is now hidden.


class ParentClass:
    def call_me(self):
        print("I am parent class")


class ChildClass(ParentClass):
    def sample(self):
        pass

pobj = ParentClass()
pobj.call_me() # output : I am parent class

cobj = ChildClass()
cobj.call_me() # I am parent class





class ParentClass:
    def call_me(self):
        print("I am parent class")


class ChildClass(ParentClass):
    def call_me(self):
        print("I am child class")

pobj = ParentClass()
pobj.call_me() # output : I am parent class

cobj = ChildClass()
cobj.call_me() # I am child class

# here the call_me() method is overridden by the child class.


# In the above code, when the call_me() method was called on the child object, the call_me() from the child class was invoked. We can invoke the parent class's call_me() method from the child class using super(), like this:

class ParentClass:
    def call_me(self):
        print("I am parent class")


class ChildClass(ParentClass):
    def call_me(self):
        print("I am child class")
        super().call_me() # using super() method to access parentclass call_me() method. 

pobj = ParentClass()
pobj.call_me() # Output: I am parent class

cobj = ChildClass()
cobj.call_me() # output :  
               # I am child class
               # I am parent class