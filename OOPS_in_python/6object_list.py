#List in object or class
#iterating over a list
class emp:
    def fun1(self):
        self.eno=int(input("enter e.no "))
        self.ename=input("enter e.name ")
        self.salary=int(input("enter e.salary "))
    def display(self):
        print("eno :",self.eno)
        print("ename:",self.ename)
        print("salary:",self.salary)
list=[]
a=int(input("Enter number of employees: "))
for i in range(a):
    obj=emp()
    obj.fun1()
    list.append(obj)
for j in list:
    print(f"""\nEmp Number: {j.eno}
Emp Name: {j.ename}
Emp salary: {j.salary}""")