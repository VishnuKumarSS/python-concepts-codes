# getting student name and details as input and printing that
# then accessing a particular student detail by using name

n = int(input("Enter no. of stud: "))
name = list(map(str,input(f"Enter {n} names : ").split()))[:n]
roll = list(map(int,input(f"Enter {n} roll numbers : ").split()))[:n]
age = list(map(int,input(f"Enter {n} ages : ").split()))[:n]
field = list(map(str,input(f"Enter {n} fields : ").split()))[:n]
dic = {}
for i in range(n):
    stud = {name[i]:{"roll":roll[i],"age":age[i],"field":field[i]}}
    dic.update(stud)
print(dic)
aa = str(input("Enter a name to find: "))
a = dic[aa]
print(a)
