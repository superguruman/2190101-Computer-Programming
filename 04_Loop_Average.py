average_of_input=0
n=0
while True:
    s=input()
    if s == "q":
        break
    average_of_input += float(s)
    n+=1
if n == 0:
    print("No Data")
else:
    print(round(average_of_input/n,2))