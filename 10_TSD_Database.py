course={}
f = open(input().strip())
for line in f:
    cid, name = [e.strip() for e in line.split(',')]
    course[cid] = name
f.close()

teacher={}
g = open(input().strip())
for line in g:
    tid, name = [e.strip() for e in line.split(',')]
    teacher[tid] = name
g.close()

h = open(input().strip())
for line in h:
    cid, tid = [e.strip() for e in line.split(',')]
    if cid not in course or tid not in teacher:
        print('record error')
    else:
        print(course[cid]+','+teacher[tid])
h.close()