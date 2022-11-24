n = 10
list1=[]
count = 0
for i in range(1,n+1):
    string = input(f"Enter string {i}: ")
    list1.append(string)
print(list1)
find = input("Enter a string to find: ")
for j in range(len(list1)):
    if list1[j] == find:
        count = count + 1
if count >0:
    print(f"The string {find} found {count} times")
elif count<=0:
    print(f"The string {find} is not found")