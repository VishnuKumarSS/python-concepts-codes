# this program is the combination of program 8 and 9.
# and to do a particular action (i.e) add employee, display all the data, display a particular employee detail


def function_emp_detail():
    action = int(input("""Enter 
1 to add employee
2 to display all data
3 to display a particular employee detail  : """))
    if action == 1:
        n=int(input("Enter number of employees: "))
        for i in range(1,n+1):
            emp_details = input(f"Enter Emp.Name, Emp.No, Emp.Dept, Emp.Salary : ").upper().split()
            emp_name = emp_details[0]
            emp_no = emp_details[1]
            emp_dept = emp_details[2]
            emp_salary = emp_details[3]
            file=open("emp_detail.txt",'a')
            file.write(f"Emp_Name:{emp_name}, Employee_Number:{emp_no}, Employee_Department:{emp_dept}, Employee_Salary:{emp_salary}\n")
            file.close()
    elif action==2:
        file = open("emp_detail.txt",'r')
        new=file.read()
        print("Emp Details: ")
        print(new)
        file.close()
    elif action==3:
        name = input("Enter your name to find in employee details: ").upper()
        # below is the method to process every word is a txt file
        f = open("emp_detail.txt", 'r')
        for line in f.readlines():
            # print("Line: ",line)
            if name in line:
                print(line)
            else:
                print("No such employee.")
            break
    else:
        print("Enter valid number :)")

function_emp_detail() # calling the function

a=1
while a==1: # to run until the user wants.
    a=int(input("""Enter
1 to run again
2 to exit  : """))
    if a == 1:
        function_emp_detail()
    elif a == 2:
        print("Exited.")
