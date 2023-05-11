month=['January','February', 'March', 'April','May','June','July','August','September','October','November','December']
date=input()
s=date.split("/")
mofu=int(s[1])-1
print(month[mofu], s[0]+',', s[2])