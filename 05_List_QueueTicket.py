q=list()
n=int(input())
time=[]
time2=[]
a=[]
ticketpos=0
callpos=0
waittime=0
ordertime=0
for k in range(n):
    c=input().split()
    if c[0] == "reset":
        a.append(int(c[1])) #reset number
    elif c[0] == "new":
        print("ticket", a[ticketpos]) #print ticket no.
        a.append(a[-1]+1) #Add next ticket number
        time.append(int(c[1])) #Add time
        time2.append(int(c[1])) #Time for order
        ticketpos+=1
    elif c[0] == "next":
        print("call", a[callpos]) #print call no.
        b=a[callpos]
        callpos+=1
    elif c[0] == "order":
        order=int(c[1])
        print("qtime", b, order-time[a.index(b)])
        waittime+=(order-time[a.index(b)])
        ordertime+=1
    else:
        avgt=waittime/ordertime
        print("avg_qtime "+ str(round(avgt,4)))