def reverse(d):
    r=dict()
    for i in d:
        r[d[i]] = i
    return r

def keys(d, v):
    a=[]
    for i in d:
        if d[i] == v:
            a.append(i)
    return a

exec(input().strip())