def dnagrader():
    code=input().strip().upper()
    op=input()
    for i in range(len(code)):
        if code[i] not in "ACTG":
            return print("Invalid DNA")
    if op == "R":
        newcode=""
        for i in range(len(code)):
            if code[i] == "A":
                newcode+="T"
            elif code[i] == "T":
                newcode+="A"
            elif code[i] == "C":
                newcode+="G"
            elif code[i] == "G":
                newcode+="C"
        newcode2=newcode[::-1]
        return print(newcode2)
    elif op == "F":
        A=0
        T=0
        C=0
        G=0
        for i in range(len(code)):
            if code[i] == "A":
                A+=1
            elif code[i] == "T":
                T+=1
            elif code[i] == "C":
                C+=1
            elif code[i] == "G":
                G+=1
        return print("A="+str(A)+", "+"T="+str(T)+", "+"G="+str(G)+", "+"C="+str(C))
    elif op == "D":
        change=input()
        n=0
        for i in range(1,len(code)):
            if code[i-1:i+1] == change:
                n+=1
        return print(n)
dnagrader()