f = open("a.txt", 'w')
line1 = 'Welcome to python'
f.write(line1)
line2="\nRegularly visit python\n"
f.write(line2)
f.close() # here the line1 and line2 are writed in variable f


f = open("a.txt", 'r')
text = f.read()
print(text)
f.close() 