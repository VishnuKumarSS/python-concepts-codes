class emp:
    def fun1(self):
        self.eno=int(input("enter eno "))
        self.ename=input("enter ename ")
        self.salary=int(input("enter esalary "))
    def display(selff):
        print("eno :",selff.eno)
        print("ename:",selff.ename)
        print("salary:",selff.salary)
obj=emp()
obj.fun1()
obj.display()

