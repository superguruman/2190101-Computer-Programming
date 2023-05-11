a=float(input())
b=a
L=0
U=0
while True:
    if b // 10 == 0:
        U+=1
        break
    if b // 10 != 0:
        U+=1
        b=b//10
while True:
    x=(L+U)/2
    if abs(a-(10**x)) <= 10**(-10)*max(a,10**x):
        print(round(x,6))
        break
    if 10**x > a:
        U = x
    else:
      10**x < a
      L = x