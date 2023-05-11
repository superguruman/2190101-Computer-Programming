sid=[]
g=[]
student=input()
while student != "q":
    studentid,grade=student.split()
    sid.append(studentid)
    g.append(grade)
    student=input()

upgrade=input().split()
mgrade=["F","D","D+","C","C+","B","B+","A","A"]
for i in upgrade:
    if i in sid:
        a=sid.index(i) #Position of student IDs in list
        b=mgrade.index(g[a]) #Use "a" to find the student's grade position
        g[a]=mgrade[b+1] #Student's grade is replaced with position+1
for z in sorted(sid):
    f=sid.index(z)
    print(sid[f], g[f])