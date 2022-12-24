a = 1
factorial = int(input("Enter a number to find the factorial: "))
for i in range(1,factorial+1):
    a = a*i
    print(f"in {i}st iteration: ",a) # to know what is happening
print("Factorial: ",a)
