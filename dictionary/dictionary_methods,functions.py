dic = { "subject": "tamil", "marks" : 75}
print(dic["marks"])
print(dic.get("subject"))
d=dic.keys()
print(d)
"""del dic["marks"]
print(dic)"""
dic.pop("subject")
print(dic)
dic.clear()
print(dic)


x=dict({"name":"starz"})
print(x)
y=dict({"name":"st"})
x.update(y)
print(x)
x.update({"age":20})
print(x)
y=x.setdefault("class",12)
print(y)
print(x)


x={"st":7,"gt":12,"sq":2,"pr":67}
y=x.setdefault("xr",22)
print(y)
print(x)
a=max(x,key=x.get)
print(a)
print(x)

z=sorted(x,key=x.get,reverse=True)
print(z)
z1=sorted(x,key=x.get)
print(z1)