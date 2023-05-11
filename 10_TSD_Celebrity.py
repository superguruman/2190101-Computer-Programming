def knows (R,x,y):
    return y in R[x]

def is_celeb(R,x):
    if len(R[x])==1 and R[x] != {x} or len(R[x])>1:
        return False
    c = sum([1 for e in R if e!=x and x in R[e]])
    return c == len(R) - 1

def find_celeb(R):
    for x in R:
        if is_celeb(R, x):  
            return x
    return None

def read_relations():
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1 : break
        u1, u2 = d
        if u1 not in R: R[u1] = set()
        if u2 not in R: R[u2] = set()
        R[u1].add(u2)

    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None:
        print('Not Found')
    else:
        print(c)

exec(input().strip()) # do not remove this line