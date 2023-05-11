first=[]
third=[]
a=[]
n=int(input())
for i in range(n):
    first.append(input())
second=input().split()
while True:
    x=input()
    if x == "-1":
        break
    third.append(x)
list=first+second+third
for i in range(len(list)):
    if i % 2 != 0:
        a.insert(0,int(list[i]))
    else:
        a.append(int(list[i]))
print(a)