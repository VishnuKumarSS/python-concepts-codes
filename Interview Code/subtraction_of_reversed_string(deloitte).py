# subtraction of reversed string

def differenceOfReverse(m1,m2):
    diff=0
    m3=str(m1)
    m4=str(m2)
    m5=m3[::-1]
    m6=m4[::-1]
    m7=int(m5)
    m8=int(m6)
    diff = m7-m8
    return diff
m1=3456
m2=1234
print(differenceOfReverse(m1,m2))
