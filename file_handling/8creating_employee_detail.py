# this program is to get the employee details and show it in output


n=int(input("Enter number of employees: "))
for i in range(1,n+1):
    emp_details = input(f"{i}.Enter Emp.Name, Emp.No, Emp.Dept, Emp.Salary : ").upper().split()
    emp_name = emp_details[0]
    emp_no = emp_details[1]
    emp_dept = emp_details[2]
    emp_salary = emp_details[3]
    file=open("emp_detail.txt",'a')
    file.write(f"{i}.Emp_Name,{emp_name},Employee_Number,{emp_no},Employee_Department,{emp_dept},Employee_Salary,{emp_salary}\n")
    file.close()

file = open("emp_detail.txt",'r')
a=file.read()
print("Emp Details: ")
print(a)
file.close()
