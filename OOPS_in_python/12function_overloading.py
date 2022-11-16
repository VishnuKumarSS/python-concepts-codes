# function overloading

def product(a, b):
    p = a * b
    print(p)
def product(a, b, c): # Here this product function actually hides the first product function 
    p = a * b * c
    print(p)
product(4, 5, 6)
product(4, 5, 5)

