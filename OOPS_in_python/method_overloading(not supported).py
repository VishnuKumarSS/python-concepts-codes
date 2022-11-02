# Method Overloading (Not supported)
# The concept of method overloading is found in almost every well-known programming language that follows object-oriented programming concepts. It simply refers to the use of many methods with the same name that take various numbers of arguments within a single class.

# Let's now understand method overloading with the help of the following code:

class OverloadingDemo:
    def add(self, x, y):
        print(x+y)

    def add(self, x, y, z):
        print(x+y+z)


obj = OverloadingDemo()
obj.add(2, 3)

# Output:

# Traceback (most recent call last):
#   File "C:\Users\ashut\Desktop\Test\hello\setup.py", line 10, in <module>
#     obj.add(2, 3)
# TypeError: add() missing 1 required positional argument: 'z'

#You're probably wondering why this happened. As a result, the error is displayed because Python only remembers 
# the most recent definition of add(self, x, y, z), which takes three parameters in addition to self. 
# As a result, three arguments must be passed to the add() method when it is called. To put it another way, it disregards the prior definition of add().

#Thus, Python doesn't support Method Overloading by default.