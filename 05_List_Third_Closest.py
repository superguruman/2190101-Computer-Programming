n=int(input())
d=[]
coord=[]
d2=[]
coord2=[]
for i in range(n):
    c=list(map(float,(input().split())))
    distance=(c[0]**2+c[1]**2)**0.5
    d.append(distance)
    coord.append(c)
for a in sorted(d):
    f=d.index(a)
    d2.append(d[f])
    coord2.append(coord[f])
s=", ".join(list(map(str,coord2[2])))
print("#"+str(coord.index(coord2[2])+1)+":"+" "+"("+str(s)+")")