korn=input()
kiak=korn[0]
arm=0
non=""
for hoon in korn:
    if hoon == kiak:
        arm+=1
    else:
        non+=kiak+" "+str(arm)+" "
        arm = 1
    kiak = hoon
new=hoon+" "+str(arm)
print(non+new)