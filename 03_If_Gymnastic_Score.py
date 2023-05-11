score=input().split()
n=list(map(float,score))
max=n[0]
min=n[0]
if max < n[1]:
    max = n[1]
if max < n[2]:
    max = n[2]
if max < n[3]:
    max = n[3]
if min > n[1]:
    min = n[1]
if min > n[2]:
    min = n[2]
if min > n[3]:
    min = n[3]
n.pop(n.index(max))
n.pop(n.index(min))
b=round(((n[0]+n[1])/2),2)
print(b)