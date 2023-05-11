M=input()
N=input()
x=len(M)
if int(x) < int(N):
    z=int(N)-int(x)
    M='0'*(z)+M
print(M)