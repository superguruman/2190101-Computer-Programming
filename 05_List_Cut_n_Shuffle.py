card=input().split()
cmd=input()
for i in cmd:
    if i == "C":
        card=card[len(card)//2:]+card[0:len(card)//2]
    elif i == "S":
        scard=[]
        for i in range(len(card)//2):
            scard.append(card[i])
            scard.append(card[i+(len(card)//2)])
        card=scard
print(" ".join(card))