x=input()
if len(x) == 10:
    if "06" in x[0:2] or "08" in x[0:2] or "09" in x[0:2]:
        print("Mobile number")
    else:
        print("Not a mobile number")
else:
    print("Not a mobile number")