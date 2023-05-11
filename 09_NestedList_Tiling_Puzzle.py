def row_number(t, e):
    for row in range(len(t)):
        if e in t[row]:
            return row
    return

def flatten(t):
    ans=[]
    for i in range(len(t)):
        for j in range(len(t[i])):
            ans.append(t[i][j])
    for k in ans:
        if k == 0:
            pos=ans.index(k)
            ans.pop(pos) 
    return ans

def inversions(x):
    n = 0
    for i in range(len(x)):
        for j in range(i+1, len(x)):
                if x[i] > x[j]:
                    n+=1
    return n

def solvable(t):
    if len(t) % 2 == 1 and inversions(flatten(t)) % 2 == 0:
        return True
    elif len(t) % 2 == 0:
        r0 = row_number(t, 0)
        if inversions(flatten(t)) % 2 == 1 and r0 % 2 == 0:
            return True
        elif inversions(flatten(t)) % 2 == 0 and r0 % 2 == 1:
            return True
    return False

exec(input().strip())