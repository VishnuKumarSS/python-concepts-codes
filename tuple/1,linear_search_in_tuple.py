# this program also search for the strings and supports strings as a input

tup1=tuple(map(str,input("Enter the tuple elements followed by space: ").split()))
#print(tup1)
num=input("Enter anything to search: ")
found = False

for i in range(len(tup1)):
    if tup1[i]==num:
        found=True
if found==True:
    print("Found")
else:
    print("not Found")
