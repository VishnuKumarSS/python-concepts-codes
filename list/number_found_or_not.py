n = 10
list1=[]
count = 0
for i in range(1,n+1):
    numbers = int(input(f"Enter number {i}: "))
    list1.append(numbers)
print(list1)
find = int(input("Enter a number to find: "))
for j in range(len(list1)):
    if list1[j] == find:
        count = count + 1
if count > 0:
    print(f"The number {find} found {count} times")
elif count<=0:
    print(f"number{find} is not found")