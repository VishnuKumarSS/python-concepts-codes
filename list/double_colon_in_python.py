string = "hellow_world_python"

print(string[::-1]) # simply reverse a string

print(string[::3]) # starts from 0 and slices index 0, 3, 6, 9,...
print(string[0::2]) # starts from beginning (i.e) 0 and slices index 0,2,4,6,...

print(string[:]) # prints the same
print(string[::]) # prints the same

print(string[0::])  # starts from beginning , and prints the same
print(string[1::]) # removes first char (i.e) index 0 from string
print(string[2::]) # removes first two char's (i.e) index 0,1 , and prints the remaining

# NEGATIVE INDEXING in DOUBLE COLON
print("reverse: ",string[::-1]) # reverse
print(string[::-2]) # reverses the string and slices 0,2,4,6,...
print(string[5::-2]) # first it cuts the string to index values upto index 5
# and it comes or starts from the end of that string
# here it cuts the string upto 5th index value (i.e) hellow
# and starts from end of the string and slices the second index from end and prints --- wle
print(string[6::-2]) # first it cuts the string to index values upto index 6
# and it comes or starts from the end of that string
# here it cuts the string upto 6th index value (i.e) hellow_
# and starts from end of the string and slices the second index from end and prints --- _olh