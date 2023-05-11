FN=["Robert","William","James","John","Margaret","Edward","Sarah","Andrew","Anthony","Deborah"]
NN=["Dick","Bill","Jim","Jack","Peggy","Ed","Sally","Andy","Tony","Debbie"]
n=int(input())
a=[]
for i in range(n):
    name=input()
    if name in FN:
        a.append(NN[FN.index(name)])
    elif name in NN:
        a.append(FN[NN.index(name)])
    else:
        a.append("Not found")
for l in range(len(a)):
    print(a[l])