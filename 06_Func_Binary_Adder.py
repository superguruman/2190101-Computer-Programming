def binary():
    a=input().split()
    x1,x2= int(a[0], 2), int(a[1], 2)
    sum=x1+x2
    return bin(sum)[2:]
print(binary())