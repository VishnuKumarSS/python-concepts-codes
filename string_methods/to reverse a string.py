count = input("Enter your count: ")
inpt = input("Enter the values followed by space: ")
array = inpt.split(' ')
a = array[::-1]
print("The reversed string is: ")
for i in a:
    print(i,end=' ')

# or 

'''count = input()
inpt = input()

array = inpt.split(' ')

# Remove empty string
#array = [i for i in array if len(i)]

# Reverse array
array.reverse()

for i in array:
    print(i, end=' ')'''
