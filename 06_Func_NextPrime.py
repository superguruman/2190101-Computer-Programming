def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True

def next_prime(n):
    n+=1
    while not is_prime(n):
        n+=1
    return n

def next_twin_prime(n):
    x=next_prime(n)
    y=next_prime(x)
    while (y-x) != 2:
        x=next_prime(x)
        y=next_prime(x)
    return x,y

exec(input().strip())