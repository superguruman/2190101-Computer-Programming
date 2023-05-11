data={}
for i in range(int(input())):
    a, b, c = input().split()
    data[a+' '+b] = c
    data[c] = a+' '+b
for i in range(int(input())):
    x = input()
    if x in data:
        print(x, "-->", data[x])
    else:
        print(x, "-->", "Not found")