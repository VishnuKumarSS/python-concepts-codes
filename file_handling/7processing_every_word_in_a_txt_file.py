a1=open("a.txt")
b=a1.read()
print(b)


# below is the method to process every word is a txt file
f = open("a.txt", 'r')
for line in f.readlines():
    print("Line: ",line)
    for word in line.split():
        print("Word: ",word)