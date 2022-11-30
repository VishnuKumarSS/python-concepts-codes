# to find a character in a list of strings
# and to print how many times it present in a string
n=10
list = []
count = 0
for i in range(1,n+1):
    string = str(input(f"Enter your string {i}: "))
    list.append(string)
print("The list of strings: ",list)
char = input("Enter a character to find in strings: ")
# to find the char in a string
for j in list:
    for k in j:
        if k == char:
            count = count + 1
if count > 0:
    print(f"The character {char} is found {count} times in list of strings")
elif count <= 0:
    print(f"The character { char } is not found in list of strings")


