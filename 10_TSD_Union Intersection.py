x = [set(int(e) for e in input().split()) for i in range(int(input()))]
if len(x) != 0:
    base = x[0]
    union = set(base)
    intersection = set(union)
    for i in range(1,len(x)):
        union |= x[i]
        intersection &= x[i]
else:
    union = {}
    intersection = {}

print(len(union))
print(len(intersection))