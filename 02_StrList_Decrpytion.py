x=input()
y=(x[3:33:7])
z=(x[7:33:5])
a=int(y)+int(z)+10000
b=str(a)
threeb=(b[-4]+b[-3]+b[-2])
c=(int(b[-2])+int(b[-3])+int(b[-4]))
d=str(c)
e=(int(d[-1])+1)
alpha=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
f=alpha[e-1]
print(threeb+f)