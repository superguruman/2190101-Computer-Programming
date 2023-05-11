L = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
R = ['N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while True:
    ans=""
    data=input()
    if data == "end":
        break
    for i in data:
        if i.islower():
            i=i.upper()
            D=True
        else:
            D=False
        if i in L:
            a=R[L.index(i)]
        elif i in R:
            a=L[R.index(i)]
        else:
            a=i
        if D == True:
            a=a.lower()
        ans+=a
    print(ans)