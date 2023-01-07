# getting student name and details as input and printing that
# then accessing by enter from 1 to 4
beginning = 0  # to force the user to get the input as 1 below
print('''Enter 1 for entering details
Enter 2 to Display the details
Enter 3 to Access
Enter 4 to exit : ''')
while beginning==0:
    start = int(input())
    if start == 1:
        beginning = 1
    else:
        print("First do Press 1 for entering the details: ")

if start == 1:
    n = int(input("Enter no. of stud: "))
    name = list(map(str,input(f"Enter {n} names : ").split()))[:n]
    roll = list(map(int,input(f"Enter {n} roll numbers : ").split()))[:n]
    age = list(map(int,input(f"Enter {n} ages : ").split()))[:n]
    field = list(map(str,input(f"Enter {n} fields : ").split()))[:n]
    # to store the entered details in a dictionary
    dic = {}
    for i in range(n):
        stud = {name[i]:{"roll":roll[i],"age":age[i],"field":field[i]}}
        dic.update(stud)

    print('''Now
Enter 2 to Display the details
Enter 3 to Access
Enter 4 to exit   : ''')
    start1 = int(input())

    if start1 == 2:
        print(dic)

        print('''Enter 3 to find and 4 to exit''')
        start2 = int(input())
        if start2 == 4:
            exit


        
    if start1 == 3 or start2 == 3:
        aa = str(input("Enter a name to find: "))
        a = dic[aa]
        print(a)

        print("Enter 4 to exit :")
        q = int(input())
        if q == 4:
            print("exited")
            exit

    if start1 == 4 :
        exit

elif start==4:
    print("exited")
    exit
elif start>4:
    print("First enter the details by pressing 1 by running again")

