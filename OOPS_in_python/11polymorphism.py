#polymorphism
# 2 types
# compile time polymorphism 
      # Overloading
# run time polymorphism
      # Overriding

# Python does not support constructor overloading
# But supports both the function and operator overloading

class Example:
      # constructor overloading based on args
      def __init__(self, *args): # Here *args is used for storing the array or list of elements
      # if args are more than 1 sum of args
            if len(args) > 1:
                  self.answer = 0
                  for i in args:
                        self.answer += i
      # if arg is an integer square the arg
            elif isinstance(args[0], int):
                  self.answer = args[0] * args[0]
      # if arg is string Print with hello
            elif isinstance(args[0], str):
                  self.answer = "Hello! " + args[0]
e1 = Example(1, 2, 3, 6, 8)
print("Sum :", e1.answer)
e2 = Example(6)
print("Square :", e2.answer)
e3 = Example("Starz.")
print("String :", e3.answer)