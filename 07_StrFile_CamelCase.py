data=input()
data2=[]
punc = [".", "?", '"', "'", "!", ",", ";", ":", "-", "(", ")", " ",">","<"]
for i in range(len(data)):
    if data[i] not in punc:
        data2.append(data[i])
    else:
        data2.append(" ")
data3="".join(data2).split()
for i in range(len(data3)):
    if data3[i][0].isupper():
        data3[i] = data3[i][0].lower() + data3[i][1:].lower()
    elif data3[i][0].islower():
        data3[i] = data3[i][0].upper() + data3[i][1:].lower()
print("".join(data3))