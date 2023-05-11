def make_int_list(x):
    y = x.split()
    a=list(map(int,y))
    return a

def is_odd(e):
    if e % 2 != 0:
        return True
    else:
        return False

def odd_list(alist):
    l=[]
    a=list(map(int,alist))
    for i in range(len(a)):
        if is_odd(a[i]) == True:
            l.append(a[i])
    return l

def sum_square(alist):
    sum=0
    a=list(map(int,alist))
    for i in range(len(a)):
        sum+=(a[i]*a[i])
    return sum

exec(input().strip())