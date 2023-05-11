def factor(N):
    k=2
    ans=[]
    while k <= N:
        if N % k == 0:
            c=0
            while N % k == 0:
                N //= k
                c +=1
            ans.append([k,c])
        k+=1
    return ans

exec(input().strip()) 