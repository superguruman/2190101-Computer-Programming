i=int(input()) #input integer
storage=[]
for a in range(i): #input value
    a=input().split()
    a=list(map(int,a))
    storage+=a
z=input() #Zig-Zag
if z == "Zig-Zag":
    print(min(storage[::4]+storage[3::4]),max(storage[1::4]+storage[2::4]))
elif z == "Zag-Zig":
    print(min(storage[1::4]+storage[2::4]),max(storage[0::4]+storage[3::4]))