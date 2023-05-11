word=input()
sentence=input().replace("\"","").replace("."," ").replace("(","").replace(")","").replace("\'","").split()
count=0
for i in range(len(sentence)):
    if sentence[i] == word:
        count+=1
print(count)