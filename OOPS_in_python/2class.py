class sample:
    name="STARZ"
    age=20
    def display(self): # we cannot access the name and age without self or arguments inside the display function
        print(self.name)
        print(self.age)
obj=sample()
obj.display()