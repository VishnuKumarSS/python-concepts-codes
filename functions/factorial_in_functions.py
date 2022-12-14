a = int(input("Enter a number to find the factorial: "))
x = 1
def factorial(a,x):
    for i in range(1,a+1):
        x *= i
    return x
print(factorial(a,x))


