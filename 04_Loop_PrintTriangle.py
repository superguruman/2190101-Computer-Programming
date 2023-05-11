h=int(input())
space1=h-1
w=2*h-1
midspace=0
base="*"*(2*h-1)
Fspace=" "*space1
print(Fspace+"*")
for doltada in range(1,space1):
    space1-=1
    Fspace=" "*space1
    midspace=" "*(2*doltada-1)
    print(Fspace+"*"+midspace+"*")
print(base)