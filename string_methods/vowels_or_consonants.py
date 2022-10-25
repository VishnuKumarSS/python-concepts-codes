# vowels or consonants using string methods

a=input("Enter a word: ")
b=a.count("a")
c=a.count("e")
d=a.count("i")
e=a.count("o")
f=a.count("u")
vowels = b+c+d+e+f
print("Vowels :",vowels)
spaces = a.count(" ")
consonants = len(a) - vowels - spaces
print("Consonants: ",consonants)


