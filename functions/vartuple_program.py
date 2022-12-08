#Variable length arguments 
def sum( *vartuple ): 
    s=0 
    for var in vartuple: 
        s=s+int(var)
    return s
r=sum( 70, 60, 50 ) 
print(r) 
r=sum(4,5)
print(r)