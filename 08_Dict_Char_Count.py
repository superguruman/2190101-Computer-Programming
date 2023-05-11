n=input().lower()
d={}
for i in n:
    if 'a' <= i <= 'z':
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
sortd=[]
for i in d:
    sortd.append([-d[i], i])
sortd.sort()
for a, b in sortd:
    print(b, "->", -a)