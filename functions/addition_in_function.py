# getting 10 number and adding that to list
# and adding list elements using function

x = 10
lis = list()
for i in range(1,10+1):
    num = int(input(f"Enter {i}st number: "))
    lis.append(num)

# here we r gonna pass the list inside the function
def adding(lis):
    added = 0
    for i in lis:
        added += i
    return added
print("Total: ",adding(lis))

