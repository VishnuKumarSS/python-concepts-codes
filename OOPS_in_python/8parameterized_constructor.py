# Parameterized constructor
class sample:
    def __init__(self,x,y): # passing arguments in a constructor is called parameterized constructor
        self.name=x
        self.age=y
    def display(selff):
        print(selff.name)
        print(selff.age)
obj=sample("Starz",20) # creating object for class sample
#There is no need to call the constructor
obj.display()
 


# same program without constructor
class sample:
    def new(self,x,y): # passing arguments 
        self.name=x
        self.age=y
    def display(selff):
        print(selff.name)
        print(selff.age)
obj=sample()
obj.new("starz",20)
obj.display()



