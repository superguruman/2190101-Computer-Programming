data={'abc':'2','def':'3','ghi':'4','jkl':'5','mno':'6','pqrs':'7','tuv':'8','wxyz':'9',' ':'0'}

def text2keys(text):
    x=""
    answer=[]
    for i in text.lower():
        if i.isalpha() or i == ' ':
            x+=i
    for j in x:
        finddata = [a for a,b in data.items() if j in a][0]
        location = finddata.index(j) + 1
        answer.append(data[finddata]*location)
    return " ".join(answer)
        
def keys2text(keys):
    a=keys.split()
    answer2=[]
    for i in a:
        number = i[0]
        pos = len(i)-1
        alpha = [a for a, b in data.items() if b == number][0][pos]
        answer2.append(alpha)
    return "".join(answer2)

#You must have this command below when submit to grader

exec(input().strip())