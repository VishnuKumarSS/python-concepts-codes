"""STRING are the sequence of characters, and which are enclosed by
either single (' ') or double quotes (" ")...
Python treats both single and double quote same"""

s = "sTarz sAmple" 

print("Upper: ",s.upper())
print("Lower: ",s.lower())


a=s.title()
b=s.count("s")
c=s.replace("sTarz","A")
d=s.find("s") # returns -1 if not found , and it returns the first accurance or low index value of occurance
d1=s.rfind("s") # returns -1 if not found , and it returns the last accurance or high index value of occurance
ddd=s.index("sA") # rises an error if not found
e=s.capitalize() # It capitalizes the first character
print("title: ",a)
print("count: ",b)
print("replace :",c)
print(f"find : {d}, rfind: {d1}")
print("index: ",ddd)
print("capitalize: ",e)


q="1a"
f=q.isalnum() # no symbols but can be alphabets or numbers
g=q.isalpha() # no symbols but it should only be alphabets
print("alpha numeric: ",f)
print("only alphabets: ",g)


h1=" "
h=h1.isspace() # returns True if it consists of only white spaces
print(h)

i="            **  star**     "
i1=i.lstrip()
i2=i.rstrip()
i3=i.strip()
print(f"i1:{i1} i2:{i2} i3:{i3}")


j = "   he is the one of the best   "
j1=j.split()
print(j1)


k="star ziiizz starzzii starzzzz"
k1=k.partition("starz") #It returns the first occurance of the characters given inside the arguments of the partition
print(k1)


l="python"
l1=l.endswith("on") # returns true or false ( boolean )
l2=l.startswith("pyo") # returns true or false ( boolean )
print("endswith : ",l1)
print("startswith : ",l2)



