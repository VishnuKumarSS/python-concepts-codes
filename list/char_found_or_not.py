n = 10
list1=[]
count = 0
for i in range(1,n+1):
    chars = input(f"Enter character {i}: ")
    list1.append(chars)
print(list1)
find = input("Enter a char to find: ")
for j in range(len(list1)):
    if list1[j] == find:
        count = count + 1
if count > 0:
    print(f"The character {find} found {count} times")
elif count <=0:
    print(f"The character{find} is not found")