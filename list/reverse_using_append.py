list1 = [5,8,3,9,2]
new_list = []
length = len(list1)
for item in list1:
    length = length-1
    new_list.append(list1[length]) #by using append
    #new_list = new_list + [list1[length]] # we can add elements to the list without using append function like this
print(new_list)