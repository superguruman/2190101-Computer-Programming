data=input().split()
peak=0
for i in range(len(data[0:-1])):
    if int(data[i-1]) < int(data[i]) and int(data[i+1]) < int(data[i]):
        peak+=1
print(peak)