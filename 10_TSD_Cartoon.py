data={}
atypes = []
while True:
    x = input()
    if x == "q":
        break
    name, atype = [e.strip() for e in x.split(",")]
    if atype not in data:
        data[atype] = []
        atypes.append(atype)
    data[atype].append(name)

for atype in atypes:
    print(atype+': '+', '.join(data[atype]))