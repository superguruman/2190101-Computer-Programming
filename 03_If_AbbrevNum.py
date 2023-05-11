x=int(input())
if x < 1000:
    print(x)
elif 1000 <= x < 10000:
    print(str(round(x/1000,1))+"K")
elif 10000 <= x < 100000:
    print(str(int(round(x/1000,0)))+"K")
elif 100000 <= x < 1000000:
    print(str(int(round(x/1000,0)))+"K")
elif 1000000 <= x < 10000000:
    print(str(round(x/1000000,1))+"M")
elif 10000000 <= x < 1000000000:
    print(str(int(round(x/1000000,0)))+"M")
elif 1000000000 <= x < 10000000000:
    print(str(round(x/1000000000,1))+"B")
else:
    print(str(int(round(x/1000000000,0)))+"B")