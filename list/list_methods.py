list = [1,2,3,4,5,5]
list.append(6)
print("append",list)
list.extend([8,9,5])
print("extend",list)
list.insert(1,11) # syntax : list.insert(index,object/value)
print("insert",list)
list.remove(5) # removes first occurance of value, here it removes number 5 from list
print("remove",list) 
list.pop(1) # removes using index value, here it removes the value in index 1
print("pop",list)
del list[4] # deletes using index value
print("delete",list)
# del list , this removes the whole list 
list.clear() # clears all the items in a list
print("clear",list)
list.extend([5,9,1,4,3])
print("Here used extend to add elements again: ",list)
list.sort() # sorts in ascending order
print("sort",list)
list.sort(reverse=True)
print("reverse sort",list)
print("length of the list: ",len(list))
print("maximum of a list : ",max(list))
print("minimum of a list : ",min(list))
print("using count in a list: ",list.count(4)) # it returns how many times the number 4 present in a list






