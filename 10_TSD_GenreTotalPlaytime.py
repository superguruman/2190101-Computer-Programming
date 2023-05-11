data = {}
for i in range(int(input())):
    a,b,genre,time= [e.strip() for e in input().split(',')]
    minute, second = [int(e) for e in time.split(':')]
    if genre not in data:
        data[genre] = 0
    data[genre] += (minute*60 + second)
ans = [(t,g) for g, t in data.items()]
ans.sort()
for t, g in ans[-3:][::-1]:
    m = str(t//60)
    s = ('0'+str(t%60))[-2:]
    print(g, '--> '+m+':'+str(s))