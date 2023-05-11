eq=input()
last=""
for i in eq:
    if i in "(":
        i = "["
    elif i in "[":
        i = "("
    elif i in ")":
        i = "]"
    elif i in "]":
        i = ")"
    last+=i
print(last)