# functions to find :
# square of a number
# square root of a number
# volume of sphere 4/3 pi r^3
# volume of cone pi r^2 h/3
def square(x):
    b = x**2
    # or 
    #b = x*x
    return b
x = int(input("Enter a number to find the square :"))
print("The square of the number is: ",square(x))


def sqroot(x):
    b = x**(1/2) # or b = x**0.5
    print(b)
y= int(input("Enter to find square root: "))
sqroot(y)


def sphere(r):
    c = (4/3)*(3.14)*(r**3)
    return c

z = int(input("Enter radius of sphere: "))
print("The volume of sphere is: ",sphere(z))


def cone(h,r):
    x = (3.14)*(r**2)*(h/3)
    return x
a = int(input("Enter the height of the cone: "))
b = int(input("Enter the radius of the cone: "))
print("The volume of cone is :",cone(a,b))
