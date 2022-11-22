'''Python has tons of standard modules. You can check out the full list of Python standard modules and their use cases. These files are in the Lib directory inside the location where you installed Python.
Standard modules can be imported the same way as we import our user-defined modules.
There are various ways to import modules. They are listed below..
Python import statement
We can import a module using the import statement and access the definitions inside it using the dot operator as described above. '''
#Here is an example.

# import statement example
# to import standard module math
import math
print("The value of pi is", math.pi)
#When you run the program, the output will be:
#The value of pi is 3.141592653589793


#Import with renaming
#import module by renaming it

import math as m
print("The value of pi is", m.pi)
#We have renamed the math module as m. This can save us typing time in some cases.
#Note that the name math is not recognized in our scope. Hence, math.pi is invalid, and m.pi is the correct implementation.

