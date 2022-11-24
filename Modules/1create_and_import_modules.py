'''What are modules in Python?

Modules refer to a file containing Python statements and definitions.
A file containing Python code, for example: example.py, is called a module, and its module name would be example.
We use modules to break down large programs into small manageable and organized files. Furthermore, modules provide reusability of code.
We can define our most used functions in a module and import it, instead of copying their definitions into different programs.'''

#Let's create a module. 
# Type the following and save it as example.py.
# Python Module example
def add(a, b):
   """This program adds two
   numbers and return the result"""
   result = a + b
   return result

'''Here, we have defined a function add() inside a module named example. The function takes in two numbers and returns their sum.'''


'''How to import modules in Python?
We can import the definitions inside a module to another module or the interactive interpreter in Python.
We use the import keyword to do this. To import our previously defined module example, we type the following in the Python prompt.'''

>>> import example
#This does not import the names of the functions defined in example directly in the current symbol table. It only imports the module name example there.

#Using the module name we can access the function using the dot . operator. For example:
>>> example.add(4,5.5)
9.5 # It returns the addition of two numbers

