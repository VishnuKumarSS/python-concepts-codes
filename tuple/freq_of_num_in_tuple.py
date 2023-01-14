#tup = tuple(map(int,input("Enter the tuple elements followed by space: ").split()))
tup = (55,7,3,2,8,76,3,55,12)
seen = []
for i in range(0,len(tup)):
    count = 1
    if tup[i] not in seen:
        for j in range(i+1,len(tup)):
            if tup[j]==tup[i]:
                count = count+1
                seen.append(tup[i])
        print(f"The number {tup[i]} present {count} times")
        