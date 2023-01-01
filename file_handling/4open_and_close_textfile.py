f = open("a.txt", 'a+')  # open text file
print(f.closed)
print(f.encoding)
print(f.mode)
print(f.newlines)
print(f.name) 

print()

f = open("a.txt", 'a+')
print(f.closed)
print("Name of the file is",f.name)
f.close() #2 close text file
print(f.closed)
