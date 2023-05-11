ic={}
for k in range(int(input())):
    a,b=input().split()
    ic[a] = float(b)
sale={}
total=0
for i in range(int(input())):
    a,b=input().split()
    if a in ic:
        p = ic[a]*int(b)
        if a in sale:
            sale[a] += p
        else:
            sale[a] = p
        total+=p
if total == 0:
    print('No ice cream sales')
else:
    print('Total ice cream sales:', total)
    a=[[sale[ic], ic] for ic in sale]
    maxmoney=max(a)[0]
    max=[]
    for x,y in a:
        if x == maxmoney:
            max.append(y)
    max.sort()
    print("Top sales:", ", ".join(max))

