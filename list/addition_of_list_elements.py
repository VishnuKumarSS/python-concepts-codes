n = 10
added = 0
list1=[]

for i in range(1,n+1):
    value = int(input(f"Enter Element {i}: "))
    list1.append(value)
print(list1)

for j in range(len(list1)):
    added = added + list1[j]
print("Added list: ",added)


