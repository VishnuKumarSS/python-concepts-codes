# this program supports only integers as input

tup1=tuple(map(int,input("Enter the tuple elements followed by space: ").split()))
#print(tup1)
num=int(input("Enter a number to search: "))
found = False

for i in range(len(tup1)):
    if tup1[i]==num:
        found=True
if found==True:
    print("Found")
else:
    print("not Found")
