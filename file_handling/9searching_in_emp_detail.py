emp=open("emp_detail.txt")
new=emp.read()
print(new)

name = input("Enter your name to find in employee details: ").upper()
# below is the method to process every word is a txt file
f = open("emp_detail.txt", 'r')
for line in f.readlines():
    # print("Line: ",line)
    if name in line:
        print(line)

    # for word in line.split("."):
    #     print("Word: ",word)