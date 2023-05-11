d={}
for k in range(int(input())):
    a, b = input().split()
    d[a] = b
    d[b] = a
for i in range(int(input())):
    n=input()
    if n in d:
        print(d[n])
    else:
        print("Not found")