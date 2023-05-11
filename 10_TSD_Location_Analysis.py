data={}
uids = []
for i in range(int(input())):
    uid, id = [e.strip() for e in input().split(":")]
    idlist = set([e.strip() for e in id.split(",")])
    data[uid] = idlist
    uids.append(uid)

qid = input().strip()
found = False
for uid in uids:
    if uid != qid and len(data[qid] & data[uid]) > 0:
        print(uid)
        found = True
if not found:
    print('Not Found')