word=input()
a=["s","x","ch"]
b=["a","e","i","o","u"]
if word[-1] in a:
    print(word+"es")
elif word[-2] == "c" and word[-1] == "h":
    print(word+"es")
elif word [-1] == "y" and word[-2] not in b:
    print(word[0:-1]+"ies")
else:
    print(word+"s")