x=list(input())
n=["0","1","2","3","4","5","6","7","8","9"]
for i in x:
    if i in n:
        n.remove(i)
if n==[]:
    print("None")
else:
    print(",".join(n))