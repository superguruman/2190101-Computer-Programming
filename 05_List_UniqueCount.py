n=[int(e) for e in input().split()]
n.sort()
ans=[n[0]]
for i in range(1,len(n)):
    if n[i] != n[i-1]:
        ans.append(n[i])
print(len(ans))
print(ans[:10])