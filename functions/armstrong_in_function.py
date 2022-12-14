a = int(input("Enter a number to find armstrong: "))
b = str(a)
c = len(b)


def armstrong(a,b,c):
    added = 0
    for j in b:
        arms = int(j)**c
        added += arms
        print("Just to know what is happening: ",arms) # This line is just to know what is happening
    if added == a:
        return "Its armstrong"
    elif added != a:
        return "Its not armstrong"


print(armstrong(a,b,c))
