string = "hellow world"
dic = dict()
for i in range(len(string)):
    if string[i] in dic:
        dic[string[i]]+=1
    else:
        dic[string[i]]=1
print(dic)
