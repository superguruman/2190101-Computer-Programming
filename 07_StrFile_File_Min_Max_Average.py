def findscore():
    a,b = input().split()
    fn = open(a, "r")
    data=[]
    line = fn.readline()
    while len(line) > 0:
        x = line.split()
        if x:
            data.append(x)
        line = fn.readline()
    score = [float(data[i][1]) for i in range(len(data)) if data[i][0][:2] == b[-2:]]
    if len(score) == 0:
        return print("No data")
    else:
        new=sorted(score)
        avg=(sum(new)/len(new))
        ans=str(new[0])+" "+str(new[-1])+" "+str(avg)
        fn.close()
        return print(ans)
findscore()